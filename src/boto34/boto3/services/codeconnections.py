"""
Wrapper for boto3 CodeConnections service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codeconnections/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_codeconnections.client import CodeConnectionsClient

from boto34.boto3.service_factory import ServiceFactory


class CodeConnectionsService(ServiceFactory[CodeConnectionsClient]):
    """
    CodeConnections service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codeconnections/)
    """
