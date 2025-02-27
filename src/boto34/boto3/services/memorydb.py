"""
Wrapper for boto3 MemoryDB service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_memorydb/)

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
    # Returns type annotated boto3 MemoryDB client
    memorydb_client = session.memorydb.client()
    memorydb_client: types_boto3_memorydb.client.MemoryDBClient
    ```
"""

from __future__ import annotations

from types_boto3_memorydb.client import MemoryDBClient

from boto34.boto3.service_factory import ServiceFactory


class MemoryDBService(ServiceFactory[MemoryDBClient]):
    SERVICE_NAME = "memorydb"
    _SERVICE_PROP = "memorydb"
