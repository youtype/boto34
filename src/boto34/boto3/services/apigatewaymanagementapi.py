"""
Wrapper for boto3 ApiGatewayManagementApi service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apigatewaymanagementapi/)

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
    # Returns type annotated boto3 ApiGatewayManagementApi client
    apigatewaymanagementapi_client = session.apigatewaymanagementapi.client()
    apigatewaymanagementapi_client: (
        types_boto3_apigatewaymanagementapi.client.ApiGatewayManagementApiClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_apigatewaymanagementapi.client import ApiGatewayManagementApiClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_apigatewaymanagementapi.client import ApiGatewayManagementApiClient
except ImportError:
    ApiGatewayManagementApiClient = object  # type: ignore[misc,assignment]


class ApiGatewayManagementApiService(
    ServiceFactory[ApiGatewayManagementApiClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "apigatewaymanagementapi"
    _SERVICE_PROP = "apigatewaymanagementapi"
