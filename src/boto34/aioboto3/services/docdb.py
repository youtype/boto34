"""
Wrapper for aioboto3 DocDB service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_docdb/)

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
    # Returns type annotated aioboto3 DocDB client
    docdb_client = session.docdb.client()
    docdb_client: types_aiobotocore_docdb.client.DocDBClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_docdb.client import DocDBClient

from boto34.aioboto3.service_factory import ServiceFactory


class DocDBService(ServiceFactory[DocDBClient]):
    SERVICE_NAME = "docdb"
    _SERVICE_PROP = "docdb"
