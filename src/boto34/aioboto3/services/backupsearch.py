"""
Wrapper for aioboto3 BackupSearch service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_backupsearch/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_backupsearch.client import BackupSearchClient

from boto34.aioboto3.service_factory import ServiceFactory


class BackupSearchService(ServiceFactory[BackupSearchClient]):
    """
    BackupSearch service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_backupsearch/)
    """
