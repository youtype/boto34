"""
Wrapper for boto3 ApiGatewayV2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apigatewayv2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_apigatewayv2.client import ApiGatewayV2Client

from boto34.boto3.service_factory import ServiceFactory


class ApiGatewayV2Service(ServiceFactory[ApiGatewayV2Client]):
    """
    ApiGatewayV2 service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apigatewayv2/)
    """
