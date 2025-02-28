"""
Wrapper for aiobotocore Backup service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_backup.client import BackupClient

from boto34.aiobotocore.service_factory import ServiceFactory


class BackupService(ServiceFactory[BackupClient]):
    """
    Backup service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/)
    """
