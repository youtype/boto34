"""
Wrapper for aiobotocore BackupSearch service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backupsearch/)

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
    # Returns type annotated aiobotocore BackupSearch client
    async with session.backupsearch.create_client() as backupsearch_client:
        backupsearch_client: types_aiobotocore_backupsearch.client.BackupSearchClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_backupsearch.client import BackupSearchClient

from boto34.aiobotocore.service_factory import ServiceFactory


class BackupSearchService(ServiceFactory[BackupSearchClient]):
    SERVICE_NAME = "backupsearch"
    _SERVICE_PROP = "backupsearch"
