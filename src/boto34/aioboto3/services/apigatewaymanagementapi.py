"""
Wrapper for aioboto3 ApiGatewayManagementApi service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_apigatewaymanagementapi/)

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
    # Returns type annotated aioboto3 ApiGatewayManagementApi client
    apigatewaymanagementapi_client = session.apigatewaymanagementapi.client()
    apigatewaymanagementapi_client: (
        types_aiobotocore_apigatewaymanagementapi.client.ApiGatewayManagementApiClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_apigatewaymanagementapi.client import ApiGatewayManagementApiClient
except ImportError:
    ApiGatewayManagementApiClient = object  # type: ignore[misc,assignment]


class ApiGatewayManagementApiService(
    ServiceFactory[ApiGatewayManagementApiClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "apigatewaymanagementapi"
    _SERVICE_PROP = "apigatewaymanagementapi"
