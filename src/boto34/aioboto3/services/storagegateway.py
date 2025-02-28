"""
Wrapper for aioboto3 StorageGateway service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_storagegateway/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_storagegateway.client import StorageGatewayClient

from boto34.aioboto3.service_factory import ServiceFactory


class StorageGatewayService(ServiceFactory[StorageGatewayClient]):
    """
    StorageGateway service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_storagegateway/)
    """
