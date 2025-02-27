"""
Wrapper for aiobotocore ApiGatewayV2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apigatewayv2/)

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
    # Returns type annotated aiobotocore ApiGatewayV2 client
    async with session.apigatewayv2.create_client() as apigatewayv2_client:
        apigatewayv2_client: types_aiobotocore_apigatewayv2.client.ApiGatewayV2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_apigatewayv2.client import ApiGatewayV2Client

from boto34.aiobotocore.service_factory import ServiceFactory


class ApiGatewayV2Service(ServiceFactory[ApiGatewayV2Client]):
    SERVICE_NAME = "apigatewayv2"
    _SERVICE_PROP = "apigatewayv2"
