"""
Wrapper for aiobotocore ApiGatewayManagementApi service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apigatewaymanagementapi/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_apigatewaymanagementapi.client import ApiGatewayManagementApiClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ApiGatewayManagementApiService(ServiceFactory[ApiGatewayManagementApiClient]):
    """
    ApiGatewayManagementApi service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apigatewaymanagementapi/)
    """
