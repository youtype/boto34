"""
Wrapper for aioboto3 MemoryDB service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_memorydb/)

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
    # Returns type annotated aioboto3 MemoryDB client
    memorydb_client = session.memorydb.client()
    memorydb_client: types_aiobotocore_memorydb.client.MemoryDBClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_memorydb.client import MemoryDBClient
except ImportError:
    MemoryDBClient = object  # type: ignore[misc,assignment]


class MemoryDBService(
    ServiceFactory[MemoryDBClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "memorydb"
    _SERVICE_PROP = "memorydb"
