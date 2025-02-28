"""
Wrapper for boto3 APIGateway service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apigateway/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_apigateway.client import APIGatewayClient

from boto34.boto3.service_factory import ServiceFactory


class APIGatewayService(ServiceFactory[APIGatewayClient]):
    """
    APIGateway service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apigateway/)
    """
