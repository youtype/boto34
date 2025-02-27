"""
Wrapper for aiobotocore ApiGatewayManagementApi service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apigatewaymanagementapi/)

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
    # Returns type annotated aiobotocore ApiGatewayManagementApi client
    async with session.apigatewaymanagementapi.create_client() as apigatewaymanagementapi_client:
        apigatewaymanagementapi_client: (
            types_aiobotocore_apigatewaymanagementapi.client.ApiGatewayManagementApiClient
        )
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_apigatewaymanagementapi.client import ApiGatewayManagementApiClient
except ImportError:
    ApiGatewayManagementApiClient = object  # type: ignore[misc,assignment]


class ApiGatewayManagementApiService(
    ServiceFactory[ApiGatewayManagementApiClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "apigatewaymanagementapi"
    _SERVICE_PROP = "apigatewaymanagementapi"
