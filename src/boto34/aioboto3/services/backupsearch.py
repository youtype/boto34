"""
Wrapper for aioboto3 BackupSearch service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_backupsearch/)

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
    # Returns type annotated aioboto3 BackupSearch client
    backupsearch_client = session.backupsearch.client()
    backupsearch_client: types_aiobotocore_backupsearch.client.BackupSearchClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_backupsearch.client import BackupSearchClient

from boto34.aioboto3.service_factory import ServiceFactory


class BackupSearchService(ServiceFactory[BackupSearchClient]):
    SERVICE_NAME = "backupsearch"
    _SERVICE_PROP = "backupsearch"
