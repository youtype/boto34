import logging
import shutil
import signal
import socket
import subprocess
import time
from collections.abc import Iterator
from typing import Any

import pytest
import requests


def get_free_tcp_port() -> int:
    sckt = socket.socket()
    sckt.bind(("", 0))
    _, port = sckt.getsockname()
    sckt.close()
    return int(port)


def start_moto_server(host: str, port: int) -> subprocess.Popen[Any]:
    logger = logging.getLogger(__name__)
    moto_svr_path = shutil.which("moto_server")
    if not moto_svr_path:
        raise ValueError(
            "Could not find a path to moto_server, is it installed in the virtualenvironment?"
        )
    args = [moto_svr_path]

    args += ["-H", host, "-p", str(port)]

    logger.info(f"Starting moto server: {args}")
    process = subprocess.Popen(
        args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )  # shell=True
    url = f"http://{host}:{port}"

    for _ in range(30):
        output = process.poll()
        if output is not None:
            logger.error(f"moto_server exited status {output}")
            stdout, stderr = process.communicate()
            logger.error(f"moto_server stdout: {stdout!s}")
            logger.error(f"moto_server stderr: {stderr!s}")
            pytest.fail("Can not start moto server")

        try:
            # we need to bypass the proxies due to monkeypatches
            requests.get(
                url,
                timeout=5,
                proxies={  # type: ignore[type-arg]
                    "http": None,
                    "https": None,
                },
            )
            break
        except requests.exceptions.ConnectionError:
            time.sleep(0.5)
    else:
        stop_process(process)
        pytest.fail("Can not start moto service")

    logger.info(f"Connected to moto server at {url}")

    return process


def stop_process(process: subprocess.Popen[Any]) -> None:
    try:
        process.send_signal(signal.SIGTERM)
        process.communicate(timeout=20)
    except subprocess.TimeoutExpired as te:
        process.kill()
        outs, errors = process.communicate(timeout=20)
        exit_code = process.returncode
        msg = f"Child process finished {exit_code} not in clean way: {outs} {errors}"
        raise RuntimeError(msg) from te


@pytest.fixture(scope="session")
def moto_server_url() -> Iterator[str]:
    host = "localhost"
    port = get_free_tcp_port()
    url = f"http://{host}:{port}"
    process = start_moto_server(host, port)

    yield url

    try:
        process.send_signal(signal.SIGTERM)
        process.communicate(timeout=20)
    except subprocess.TimeoutExpired as te:
        process.kill()
        outs, errors = process.communicate(timeout=20)
        exit_code = process.returncode
        msg = f"Child process finished {exit_code} not in clean way: {outs} {errors}"
        raise RuntimeError(msg) from te
