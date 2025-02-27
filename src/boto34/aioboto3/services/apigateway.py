"""
Wrapper for aioboto3 APIGateway service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_apigateway/)

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
    # Returns type annotated aioboto3 APIGateway client
    apigateway_client = session.apigateway.client()
    apigateway_client: types_aiobotocore_apigateway.client.APIGatewayClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_apigateway.client import APIGatewayClient
except ImportError:
    APIGatewayClient = object  # type: ignore[misc,assignment]


class APIGatewayService(
    ServiceFactory[APIGatewayClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "apigateway"
    _SERVICE_PROP = "apigateway"
