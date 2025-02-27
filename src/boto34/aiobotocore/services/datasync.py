"""
Wrapper for aiobotocore DataSync service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/)

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
    # Returns type annotated aiobotocore DataSync client
    async with session.datasync.create_client() as datasync_client:
        datasync_client: types_aiobotocore_datasync.client.DataSyncClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_datasync.client import DataSyncClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DataSyncService(ServiceFactory[DataSyncClient]):
    SERVICE_NAME = "datasync"
    _SERVICE_PROP = "datasync"
