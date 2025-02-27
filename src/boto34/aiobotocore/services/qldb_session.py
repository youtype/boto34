"""
Wrapper for aiobotocore QLDBSession service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qldb_session/)

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
    # Returns type annotated aiobotocore QLDBSession client
    async with session.qldb_session.create_client() as qldb_session_client:
        qldb_session_client: types_aiobotocore_qldb_session.client.QLDBSessionClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_qldb_session.client import QLDBSessionClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_qldb_session.client import QLDBSessionClient
except ImportError:
    QLDBSessionClient = object  # type: ignore[misc,assignment]


class QLDBSessionService(
    ServiceFactory[QLDBSessionClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "qldb-session"
    _SERVICE_PROP = "qldb_session"
