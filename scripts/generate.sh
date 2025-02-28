#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd $ROOT_PATH

cd ../mypy_boto3_builder
uvx --with ruff --with boto3 mypy-boto3-builder ../boto34/src --product boto34-boto3
uvx --with ruff --with aiobotocore mypy-boto3-builder ../boto34/src --product boto34-aiobotocore
uvx --with ruff --with aioboto3 mypy-boto3-builder ../boto34/src --product boto34-aioboto3
cd -

mv ./src/boto34/services.md ./docs/services.md