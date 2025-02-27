"""
Wrapper for aioboto3 StorageGateway service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_storagegateway/)

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
    # Returns type annotated aioboto3 StorageGateway client
    storagegateway_client = session.storagegateway.client()
    storagegateway_client: types_aiobotocore_storagegateway.client.StorageGatewayClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_storagegateway.client import StorageGatewayClient

from boto34.aioboto3.service_factory import ServiceFactory


class StorageGatewayService(ServiceFactory[StorageGatewayClient]):
    SERVICE_NAME = "storagegateway"
    _SERVICE_PROP = "storagegateway"
