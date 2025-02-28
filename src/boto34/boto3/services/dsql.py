"""
Wrapper for boto3 AuroraDSQL service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_dsql/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_dsql.client import AuroraDSQLClient

from boto34.boto3.service_factory import ServiceFactory


class AuroraDSQLService(ServiceFactory[AuroraDSQLClient]):
    """
    AuroraDSQL service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_dsql/)
    """
