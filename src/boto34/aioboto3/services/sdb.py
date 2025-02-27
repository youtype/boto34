"""
Wrapper for aioboto3 SimpleDB service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sdb/)

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
    # Returns type annotated aioboto3 SimpleDB client
    sdb_client = session.sdb.client()
    sdb_client: types_aiobotocore_sdb.client.SimpleDBClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_sdb.client import SimpleDBClient

from boto34.aioboto3.service_factory import ServiceFactory


class SimpleDBService(ServiceFactory[SimpleDBClient]):
    SERVICE_NAME = "sdb"
    _SERVICE_PROP = "sdb"
