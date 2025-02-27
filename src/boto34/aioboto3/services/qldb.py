"""
Wrapper for aioboto3 QLDB service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_qldb/)

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
    # Returns type annotated aioboto3 QLDB client
    qldb_client = session.qldb.client()
    qldb_client: types_aiobotocore_qldb.client.QLDBClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_qldb.client import QLDBClient

from boto34.aioboto3.service_factory import ServiceFactory


class QLDBService(ServiceFactory[QLDBClient]):
    SERVICE_NAME = "qldb"
    _SERVICE_PROP = "qldb"
