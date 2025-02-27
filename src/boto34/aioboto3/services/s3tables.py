"""
Wrapper for aioboto3 S3Tables service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_s3tables/)

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
    # Returns type annotated aioboto3 S3Tables client
    s3tables_client = session.s3tables.client()
    s3tables_client: types_aiobotocore_s3tables.client.S3TablesClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_s3tables.client import S3TablesClient

from boto34.aioboto3.service_factory import ServiceFactory


class S3TablesService(ServiceFactory[S3TablesClient]):
    SERVICE_NAME = "s3tables"
    _SERVICE_PROP = "s3tables"
