"""
Wrapper for aiobotocore QLDB service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qldb/)

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
    # Returns type annotated aiobotocore QLDB client
    async with session.qldb.create_client() as qldb_client:
        qldb_client: types_aiobotocore_qldb.client.QLDBClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_qldb.client import QLDBClient

from boto34.aiobotocore.service_factory import ServiceFactory


class QLDBService(ServiceFactory[QLDBClient]):
    SERVICE_NAME = "qldb"
    _SERVICE_PROP = "qldb"
