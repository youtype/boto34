"""
Wrapper for aiobotocore BackupSearch service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backupsearch/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_backupsearch.client import BackupSearchClient

from boto34.aiobotocore.service_factory import ServiceFactory


class BackupSearchService(ServiceFactory[BackupSearchClient]):
    """
    BackupSearch service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backupsearch/)
    """
