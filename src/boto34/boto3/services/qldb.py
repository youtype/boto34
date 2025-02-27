"""
Wrapper for boto3 QLDB service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_qldb/)

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
    # Returns type annotated boto3 QLDB client
    qldb_client = session.qldb.client()
    qldb_client: types_boto3_qldb.client.QLDBClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_qldb.client import QLDBClient
except ImportError:
    QLDBClient = object  # type: ignore[misc,assignment]


class QLDBService(
    ServiceFactory[QLDBClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "qldb"
    _SERVICE_PROP = "qldb"
