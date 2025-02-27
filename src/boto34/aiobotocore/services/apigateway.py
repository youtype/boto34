"""
Wrapper for aiobotocore APIGateway service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apigateway/)

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
    # Returns type annotated aiobotocore APIGateway client
    async with session.apigateway.create_client() as apigateway_client:
        apigateway_client: types_aiobotocore_apigateway.client.APIGatewayClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_apigateway.client import APIGatewayClient
except ImportError:
    APIGatewayClient = object  # type: ignore[misc,assignment]


class APIGatewayService(
    ServiceFactory[APIGatewayClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "apigateway"
    _SERVICE_PROP = "apigateway"
