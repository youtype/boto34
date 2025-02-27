"""
Wrapper for boto3 AuroraDSQL service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_dsql/)

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
    # Returns type annotated boto3 AuroraDSQL client
    dsql_client = session.dsql.client()
    dsql_client: types_boto3_dsql.client.AuroraDSQLClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_dsql.client import AuroraDSQLClient
except ImportError:
    AuroraDSQLClient = object  # type: ignore[misc,assignment]


class AuroraDSQLService(
    ServiceFactory[AuroraDSQLClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "dsql"
    _SERVICE_PROP = "dsql"
