"""
Wrapper for boto3 Lambda service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lambda/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 Lambda client
    lambda_client = session.lambda_.client()
    lambda_client: types_boto3_lambda.client.LambdaClient
    ```
"""

from __future__ import annotations

from types_boto3_lambda.client import LambdaClient

from boto34.boto3.service_factory import ServiceFactory


class LambdaService(ServiceFactory[LambdaClient]):
    SERVICE_NAME = "lambda"
    _SERVICE_PROP = "lambda_"
