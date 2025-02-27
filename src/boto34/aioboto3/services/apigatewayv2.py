"""
Wrapper for aioboto3 ApiGatewayV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_apigatewayv2/)

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
    # Returns type annotated aioboto3 ApiGatewayV2 client
    apigatewayv2_client = session.apigatewayv2.client()
    apigatewayv2_client: types_aiobotocore_apigatewayv2.client.ApiGatewayV2Client
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_apigatewayv2.client import ApiGatewayV2Client
except ImportError:
    ApiGatewayV2Client = object  # type: ignore[misc,assignment]


class ApiGatewayV2Service(
    ServiceFactory[ApiGatewayV2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "apigatewayv2"
    _SERVICE_PROP = "apigatewayv2"
