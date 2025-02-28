"""
Wrapper for aioboto3 Backup service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_backup/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_backup.client import BackupClient

from boto34.aioboto3.service_factory import ServiceFactory


class BackupService(ServiceFactory[BackupClient]):
    """
    Backup service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_backup/)
    """
