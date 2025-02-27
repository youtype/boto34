"""
Wrapper for aioboto3 Lambda service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lambda/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 Lambda client
    lambda_client = session.lambda_.client()
    lambda_client: types_aiobotocore_lambda.client.LambdaClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_lambda.client import LambdaClient

from boto34.aioboto3.service_factory import ServiceFactory


class LambdaService(ServiceFactory[LambdaClient]):
    SERVICE_NAME = "lambda"
    _SERVICE_PROP = "lambda_"
