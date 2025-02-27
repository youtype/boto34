"""
Wrapper for aioboto3 QLDBSession service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_qldb_session/)

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
    # Returns type annotated aioboto3 QLDBSession client
    qldb_session_client = session.qldb_session.client()
    qldb_session_client: types_aiobotocore_qldb_session.client.QLDBSessionClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_qldb_session.client import QLDBSessionClient
except ImportError:
    QLDBSessionClient = object  # type: ignore[misc,assignment]


class QLDBSessionService(
    ServiceFactory[QLDBSessionClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "qldb-session"
    _SERVICE_PROP = "qldb_session"
