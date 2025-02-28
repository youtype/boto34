"""
Wrapper for boto3 BackupSearch service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_backupsearch/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_backupsearch.client import BackupSearchClient

from boto34.boto3.service_factory import ServiceFactory


class BackupSearchService(ServiceFactory[BackupSearchClient]):
    """
    BackupSearch service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_backupsearch/)
    """
