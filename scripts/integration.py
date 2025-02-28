#!/usr/bin/env python
# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "loguru",
# ]
# ///
"""
Integration tests.

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import argparse
import difflib
import json
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Sequence

from loguru import logger

ROOT_PATH = Path(__file__).parent.parent.resolve()
PYRIGHT_CONFIG_PATH = Path(__file__).parent / "pyrightconfig_output.json"


class SnapshotMismatchError(Exception):
    """
    Exception for e2e failures.
    """

    def __init__(self, path: Path) -> None:
        super().__init__(f"Snapshot {path} is different")


@dataclass
class Product:
    """
    Library to test.
    """

    name: str
    with_packages: list[str] = field(default_factory=list)

    @property
    def sample_path(self) -> Path:
        return ROOT_PATH / "e2e" / self.name / "sample.py"

    @property
    def mypy_path(self) -> Path:
        return ROOT_PATH / "e2e" / self.name / "mypy.log"

    @property
    def pyright_path(self) -> Path:
        return ROOT_PATH / "e2e" / self.name / "pyright.json"


PRODUCTS = [
    Product(name="boto3", with_packages=["boto3", "types-boto3-lite", "types-boto3-full"]),
    Product(
        name="aiobotocore",
        with_packages=["aiobotocore", "types-aiobotocore-lite", "types-aiobotocore-full"],
    ),
    Product(
        name="aioboto3",
        with_packages=[
            "aioboto3",
            "types-boto3-lite",
            "types-aioboto3-lite",
            "types-aiobotocore-full",
        ],
    ),
]


@dataclass
class CLINamespace:
    """
    CLI namespace.
    """

    log_level: str
    update: bool
    products: list[str] | None
    python_version: str | None


def parse_args() -> CLINamespace:
    """
    CLI parser.
    """
    parser = argparse.ArgumentParser(__file__)
    parser.add_argument("-d", "--debug", action="store_true", help="Show debug messages")
    parser.add_argument("-u", "--update", action="store_true")
    parser.add_argument(
        "-p",
        "--product",
        nargs="*",
        choices=[i.name for i in PRODUCTS],
        default=None,
    )
    parser.add_argument(
        "--python",
        type=str,
        default=None,
        help="Python version for checkers. Default: None",
    )

    args = parser.parse_args()

    return CLINamespace(
        log_level="DEBUG" if args.debug else "INFO",
        update=args.update,
        products=args.product,
        python_version=args.python,
    )


def print_path(path: Path) -> str:
    """
    Get path as a string relative to current workdir.
    """
    if path.is_absolute():
        cwd = Path.cwd()
        if path == cwd or path.parts <= cwd.parts:
            return path.as_posix()

        try:
            path = path.relative_to(cwd)
        except ValueError:
            return str(path)

    if len(path.parts) == 1:
        return f"./{path.as_posix()}"

    return path.as_posix()


def compare(data: str, snapshot_path: Path, *, update: bool) -> None:
    """
    Compare tool output with a snapshot.
    """
    data = data.strip()
    if not snapshot_path.exists():
        snapshot_path.write_text(data)
        logger.info(f"Created {print_path(snapshot_path)}")
        return

    old_data = snapshot_path.read_text().strip()
    if old_data == data:
        logger.debug(f"Matched {print_path(snapshot_path)}")
        return

    if update:
        snapshot_path.write_text(data)
        logger.info(f"Updated {print_path(snapshot_path)}")
        return

    diff = difflib.unified_diff(
        old_data.strip().splitlines(),
        data.strip().splitlines(),
        lineterm="",
    )
    for line in diff:
        logger.warning(line)
    raise SnapshotMismatchError(snapshot_path)


def run_mypy(path: Path, snapshot_path: Path, *, update: bool, uvx_args: Sequence[str]) -> None:
    """
    Run `mypy` and compare output.
    """
    cmd = ["uvx", *uvx_args, "mypy", path.as_posix(), "--no-incremental"]
    logger.debug(f"Running process: {' '.join(cmd)}")
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, encoding="utf8")
    except subprocess.CalledProcessError as e:
        output = e.output

    new_data_lines: list[str] = []
    for line in output.splitlines():
        if line.endswith("defined here"):
            continue
        new_data_lines.append(line)
    new_data = "\n".join(new_data_lines)
    compare(new_data, snapshot_path, update=update)


def run_pyright(path: Path, snapshot_path: Path, *, update: bool, uvx_args: Sequence[str]) -> None:
    """
    Run `pyright` and compare output.
    """
    config_path = ROOT_PATH / "pyrightconfig.json"
    shutil.copyfile(PYRIGHT_CONFIG_PATH, config_path)
    cmd = ["uvx", *uvx_args, "pyright", path.as_posix(), "--outputjson"]
    logger.debug(f"Running process: {' '.join(cmd)}")
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL, encoding="utf8")
    except subprocess.CalledProcessError as e:
        output = e.output
    finally:
        Path(config_path).unlink(missing_ok=True)

    data = json.loads(output).get("generalDiagnostics", [])
    for diag in data:
        if "file" in diag:
            del diag["file"]
        if "uri" in diag:
            del diag["uri"]

    new_data = json.dumps(data, indent=4)
    compare(new_data, snapshot_path, update=update)


def main() -> None:
    args = parse_args()
    logger.configure(
        handlers=[
            {
                "sink": sys.stderr,
                "level": args.log_level,
                "format": (
                    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
                    "<level>{level: <8}</level> | "
                    f"<cyan>{Path(__file__).stem}</cyan> - "
                    "<white>{message}</white>"
                ),
            }
        ]
    )

    for product in PRODUCTS:
        if args.products and product.name not in args.products:
            continue
        product_path = ROOT_PATH / "e2e" / product.name
        logger.info(f"Testing {product.name} integration")

        uvx_args: list[str] = ["-q"]
        if args.python_version:
            uvx_args.extend(["--python", args.python_version])
        uvx_args.extend(["--with", "."])
        for package in product.with_packages:
            uvx_args.extend(["--with", package])

        run_mypy(
            product_path / "sample.py",
            product_path / "mypy.log",
            update=args.update,
            uvx_args=uvx_args,
        )
        run_pyright(
            product_path / "sample.py",
            product_path / "pyright.json",
            update=args.update,
            uvx_args=uvx_args,
        )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
