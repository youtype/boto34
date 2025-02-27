"""
Wrapper for boto3 QLDBSession service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_qldb_session/)

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
    # Returns type annotated boto3 QLDBSession client
    qldb_session_client = session.qldb_session.client()
    qldb_session_client: types_boto3_qldb_session.client.QLDBSessionClient
    ```
"""

from __future__ import annotations

from types_boto3_qldb_session.client import QLDBSessionClient

from boto34.boto3.service_factory import ServiceFactory


class QLDBSessionService(ServiceFactory[QLDBSessionClient]):
    SERVICE_NAME = "qldb-session"
    _SERVICE_PROP = "qldb_session"
