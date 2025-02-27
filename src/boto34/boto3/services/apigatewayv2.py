"""
Wrapper for boto3 ApiGatewayV2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apigatewayv2/)

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
    # Returns type annotated boto3 ApiGatewayV2 client
    apigatewayv2_client = session.apigatewayv2.client()
    apigatewayv2_client: types_boto3_apigatewayv2.client.ApiGatewayV2Client
    ```
"""

from __future__ import annotations

from types_boto3_apigatewayv2.client import ApiGatewayV2Client

from boto34.boto3.service_factory import ServiceFactory


class ApiGatewayV2Service(ServiceFactory[ApiGatewayV2Client]):
    SERVICE_NAME = "apigatewayv2"
    _SERVICE_PROP = "apigatewayv2"
