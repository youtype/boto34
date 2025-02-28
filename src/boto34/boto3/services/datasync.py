"""
Wrapper for boto3 DataSync service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_datasync/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_datasync.client import DataSyncClient

from boto34.boto3.service_factory import ServiceFactory


class DataSyncService(ServiceFactory[DataSyncClient]):
    """
    DataSync service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_datasync/)
    """
