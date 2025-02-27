"""
Wrapper for boto3 StorageGateway service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_storagegateway/)

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
    # Returns type annotated boto3 StorageGateway client
    storagegateway_client = session.storagegateway.client()
    storagegateway_client: types_boto3_storagegateway.client.StorageGatewayClient
    ```
"""

from __future__ import annotations

from types_boto3_storagegateway.client import StorageGatewayClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_storagegateway.client import StorageGatewayClient
except ImportError:
    StorageGatewayClient = object  # type: ignore[misc,assignment]


class StorageGatewayService(
    ServiceFactory[StorageGatewayClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "storagegateway"
    _SERVICE_PROP = "storagegateway"
