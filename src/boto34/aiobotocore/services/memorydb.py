"""
Wrapper for aiobotocore MemoryDB service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_memorydb/)

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
    # Returns type annotated aiobotocore MemoryDB client
    async with session.memorydb.create_client() as memorydb_client:
        memorydb_client: types_aiobotocore_memorydb.client.MemoryDBClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_memorydb.client import MemoryDBClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_memorydb.client import MemoryDBClient
except ImportError:
    MemoryDBClient = object  # type: ignore[misc,assignment]


class MemoryDBService(
    ServiceFactory[MemoryDBClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "memorydb"
    _SERVICE_PROP = "memorydb"
