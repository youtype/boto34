#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd $ROOT_PATH

cd ../mypy_boto3_builder
uv run mypy_boto3_builder ../boto34/src --product boto34-boto3
uv run mypy_boto3_builder ../boto34/src --product boto34-aiobotocore
uv run mypy_boto3_builder ../boto34/src --product boto34-aioboto3
cd -

mv src/boto34/services.md ./services.md