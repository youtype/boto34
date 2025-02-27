"""
Wrapper for boto3 SimpleDB service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sdb/)

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
    # Returns type annotated boto3 SimpleDB client
    sdb_client = session.sdb.client()
    sdb_client: types_boto3_sdb.client.SimpleDBClient
    ```
"""

from __future__ import annotations

from types_boto3_sdb.client import SimpleDBClient

from boto34.boto3.service_factory import ServiceFactory


class SimpleDBService(ServiceFactory[SimpleDBClient]):
    SERVICE_NAME = "sdb"
    _SERVICE_PROP = "sdb"
