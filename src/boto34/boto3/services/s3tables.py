"""
Wrapper for boto3 S3Tables service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_s3tables/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_s3tables.client import S3TablesClient

from boto34.boto3.service_factory import ServiceFactory


class S3TablesService(ServiceFactory[S3TablesClient]):
    """
    S3Tables service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_s3tables/)
    """
