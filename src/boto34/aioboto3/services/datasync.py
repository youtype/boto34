"""
Wrapper for aioboto3 DataSync service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_datasync/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_datasync.client import DataSyncClient

from boto34.aioboto3.service_factory import ServiceFactory


class DataSyncService(ServiceFactory[DataSyncClient]):
    """
    DataSync service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_datasync/)
    """
