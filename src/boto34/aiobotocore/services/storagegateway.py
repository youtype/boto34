"""
Wrapper for aiobotocore StorageGateway service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore StorageGateway client
    async with session.storagegateway.create_client() as storagegateway_client:
        storagegateway_client: types_aiobotocore_storagegateway.client.StorageGatewayClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_storagegateway.client import StorageGatewayClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_storagegateway.client import StorageGatewayClient
except ImportError:
    StorageGatewayClient = object  # type: ignore[misc,assignment]


class StorageGatewayService(
    ServiceFactory[StorageGatewayClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "storagegateway"
    _SERVICE_PROP = "storagegateway"
