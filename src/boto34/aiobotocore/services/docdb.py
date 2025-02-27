"""
Wrapper for aiobotocore DocDB service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_docdb/)

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
    # Returns type annotated aiobotocore DocDB client
    async with session.docdb.create_client() as docdb_client:
        docdb_client: types_aiobotocore_docdb.client.DocDBClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_docdb.client import DocDBClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DocDBService(ServiceFactory[DocDBClient]):
    SERVICE_NAME = "docdb"
    _SERVICE_PROP = "docdb"
