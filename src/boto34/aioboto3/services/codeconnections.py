"""
Wrapper for aioboto3 CodeConnections service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codeconnections/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_codeconnections.client import CodeConnectionsClient

from boto34.aioboto3.service_factory import ServiceFactory


class CodeConnectionsService(ServiceFactory[CodeConnectionsClient]):
    """
    CodeConnections service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codeconnections/)
    """
