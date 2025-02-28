"""
Wrapper for boto3 StorageGateway service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_storagegateway/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_storagegateway.client import StorageGatewayClient

from boto34.boto3.service_factory import ServiceFactory


class StorageGatewayService(ServiceFactory[StorageGatewayClient]):
    """
    StorageGateway service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_storagegateway/)
    """
