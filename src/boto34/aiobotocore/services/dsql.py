"""
Wrapper for aiobotocore AuroraDSQL service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dsql/)

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
    # Returns type annotated aiobotocore AuroraDSQL client
    async with session.dsql.create_client() as dsql_client:
        dsql_client: types_aiobotocore_dsql.client.AuroraDSQLClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_dsql.client import AuroraDSQLClient
except ImportError:
    AuroraDSQLClient = object  # type: ignore[misc,assignment]


class AuroraDSQLService(
    ServiceFactory[AuroraDSQLClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "dsql"
    _SERVICE_PROP = "dsql"
