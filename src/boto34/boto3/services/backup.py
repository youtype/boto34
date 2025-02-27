"""
Wrapper for boto3 Backup service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_backup/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 Backup client
    backup_client = session.backup.client()
    backup_client: types_boto3_backup.client.BackupClient
    ```
"""

from __future__ import annotations

from types_boto3_backup.client import BackupClient

from boto34.boto3.service_factory import ServiceFactory


class BackupService(ServiceFactory[BackupClient]):
    SERVICE_NAME = "backup"
    _SERVICE_PROP = "backup"
