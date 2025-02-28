"""
Wrapper for aioboto3 APIGateway service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_apigateway/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_apigateway.client import APIGatewayClient

from boto34.aioboto3.service_factory import ServiceFactory


class APIGatewayService(ServiceFactory[APIGatewayClient]):
    """
    APIGateway service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_apigateway/)
    """
