"""
Wrapper for aioboto3 AuroraDSQL service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_dsql/)

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
    # Returns type annotated aioboto3 AuroraDSQL client
    dsql_client = session.dsql.client()
    dsql_client: types_aiobotocore_dsql.client.AuroraDSQLClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_dsql.client import AuroraDSQLClient

from boto34.aioboto3.service_factory import ServiceFactory


class AuroraDSQLService(ServiceFactory[AuroraDSQLClient]):
    SERVICE_NAME = "dsql"
    _SERVICE_PROP = "dsql"
