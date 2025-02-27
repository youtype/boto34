"""
Wrapper for boto3 DocDB service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_docdb/)

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
    # Returns type annotated boto3 DocDB client
    docdb_client = session.docdb.client()
    docdb_client: types_boto3_docdb.client.DocDBClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_docdb.client import DocDBClient
except ImportError:
    DocDBClient = object  # type: ignore[misc,assignment]


class DocDBService(
    ServiceFactory[DocDBClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "docdb"
    _SERVICE_PROP = "docdb"
