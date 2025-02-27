"""
Wrapper for aioboto3 Backup service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_backup/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 Backup client
    backup_client = session.backup.client()
    backup_client: types_aiobotocore_backup.client.BackupClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_backup.client import BackupClient

from boto34.aioboto3.service_factory import ServiceFactory


class BackupService(ServiceFactory[BackupClient]):
    SERVICE_NAME = "backup"
    _SERVICE_PROP = "backup"
