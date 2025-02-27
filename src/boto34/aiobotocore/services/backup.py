"""
Wrapper for aiobotocore Backup service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore Backup client
    async with session.backup.create_client() as backup_client:
        backup_client: types_aiobotocore_backup.client.BackupClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_backup.client import BackupClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_backup.client import BackupClient
except ImportError:
    BackupClient = object  # type: ignore[misc,assignment]


class BackupService(
    ServiceFactory[BackupClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "backup"
    _SERVICE_PROP = "backup"
