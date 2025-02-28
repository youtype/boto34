"""
Wrapper for boto3 QLDB service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_qldb/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_qldb.client import QLDBClient

from boto34.boto3.service_factory import ServiceFactory


class QLDBService(ServiceFactory[QLDBClient]):
    """
    QLDB service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_qldb/)
    """
