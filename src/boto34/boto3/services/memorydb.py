"""
Wrapper for boto3 MemoryDB service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_memorydb/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_memorydb.client import MemoryDBClient

from boto34.boto3.service_factory import ServiceFactory


class MemoryDBService(ServiceFactory[MemoryDBClient]):
    """
    MemoryDB service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_memorydb/)
    """
