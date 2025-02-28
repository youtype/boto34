"""
Wrapper for aioboto3 ApiGatewayV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_apigatewayv2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_apigatewayv2.client import ApiGatewayV2Client

from boto34.aioboto3.service_factory import ServiceFactory


class ApiGatewayV2Service(ServiceFactory[ApiGatewayV2Client]):
    """
    ApiGatewayV2 service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_apigatewayv2/)
    """
