"""
Wrapper for aioboto3 DataSync service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_datasync/)

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
    # Returns type annotated aioboto3 DataSync client
    datasync_client = session.datasync.client()
    datasync_client: types_aiobotocore_datasync.client.DataSyncClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_datasync.client import DataSyncClient

from boto34.aioboto3.service_factory import ServiceFactory


class DataSyncService(ServiceFactory[DataSyncClient]):
    SERVICE_NAME = "datasync"
    _SERVICE_PROP = "datasync"
