"""
Wrapper for boto3 Backup service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_backup/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_backup.client import BackupClient

from boto34.boto3.service_factory import ServiceFactory


class BackupService(ServiceFactory[BackupClient]):
    """
    Backup service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_backup/)
    """
