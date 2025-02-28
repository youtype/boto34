"""
Wrapper for boto3 SimpleDB service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sdb/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_sdb.client import SimpleDBClient

from boto34.boto3.service_factory import ServiceFactory


class SimpleDBService(ServiceFactory[SimpleDBClient]):
    """
    SimpleDB service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sdb/)
    """
