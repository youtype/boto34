"""
Wrapper for boto3 APIGateway service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apigateway/)

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
    # Returns type annotated boto3 APIGateway client
    apigateway_client = session.apigateway.client()
    apigateway_client: types_boto3_apigateway.client.APIGatewayClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_apigateway.client import APIGatewayClient
except ImportError:
    APIGatewayClient = object  # type: ignore[misc,assignment]


class APIGatewayService(
    ServiceFactory[APIGatewayClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "apigateway"
    _SERVICE_PROP = "apigateway"
