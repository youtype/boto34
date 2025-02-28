"""
Wrapper for boto3 ApiGatewayManagementApi service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apigatewaymanagementapi/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_apigatewaymanagementapi.client import ApiGatewayManagementApiClient

from boto34.boto3.service_factory import ServiceFactory


class ApiGatewayManagementApiService(ServiceFactory[ApiGatewayManagementApiClient]):
    """
    ApiGatewayManagementApi service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apigatewaymanagementapi/)
    """
