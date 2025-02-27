"""
Wrapper for aiobotocore Lambda service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lambda/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore Lambda client
    async with session.lambda_.create_client() as lambda_client:
        lambda_client: types_aiobotocore_lambda.client.LambdaClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_lambda.client import LambdaClient

from boto34.aiobotocore.service_factory import ServiceFactory


class LambdaService(ServiceFactory[LambdaClient]):
    SERVICE_NAME = "lambda"
    _SERVICE_PROP = "lambda_"
