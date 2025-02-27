"""
Wrapper for boto3 S3Tables service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_s3tables/)

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
    # Returns type annotated boto3 S3Tables client
    s3tables_client = session.s3tables.client()
    s3tables_client: types_boto3_s3tables.client.S3TablesClient
    ```
"""

from __future__ import annotations

from types_boto3_s3tables.client import S3TablesClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_s3tables.client import S3TablesClient
except ImportError:
    S3TablesClient = object  # type: ignore[misc,assignment]


class S3TablesService(
    ServiceFactory[S3TablesClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "s3tables"
    _SERVICE_PROP = "s3tables"
