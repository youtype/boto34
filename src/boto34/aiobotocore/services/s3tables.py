"""
Wrapper for aiobotocore S3Tables service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3tables/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_s3tables.client import S3TablesClient

from boto34.aiobotocore.service_factory import ServiceFactory


class S3TablesService(ServiceFactory[S3TablesClient]):
    """
    S3Tables service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3tables/)
    """
