"""
Wrapper for aiobotocore S3Tables service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3tables/)

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
    # Returns type annotated aiobotocore S3Tables client
    async with session.s3tables.create_client() as s3tables_client:
        s3tables_client: types_aiobotocore_s3tables.client.S3TablesClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_s3tables.client import S3TablesClient

from boto34.aiobotocore.service_factory import ServiceFactory


class S3TablesService(ServiceFactory[S3TablesClient]):
    SERVICE_NAME = "s3tables"
    _SERVICE_PROP = "s3tables"
