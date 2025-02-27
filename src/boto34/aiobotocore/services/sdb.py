"""
Wrapper for aiobotocore SimpleDB service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sdb/)

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
    # Returns type annotated aiobotocore SimpleDB client
    async with session.sdb.create_client() as sdb_client:
        sdb_client: types_aiobotocore_sdb.client.SimpleDBClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_sdb.client import SimpleDBClient
except ImportError:
    SimpleDBClient = object  # type: ignore[misc,assignment]


class SimpleDBService(
    ServiceFactory[SimpleDBClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sdb"
    _SERVICE_PROP = "sdb"
