"""
Wrapper for boto3 DocDB service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_docdb/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_docdb.client import DocDBClient

from boto34.boto3.service_factory import ServiceFactory


class DocDBService(ServiceFactory[DocDBClient]):
    """
    DocDB service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_docdb/)
    """
