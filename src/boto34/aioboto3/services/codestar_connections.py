"""
Wrapper for aioboto3 CodeStarconnections service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codestar_connections/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_codestar_connections.client import CodeStarconnectionsClient

from boto34.aioboto3.service_factory import ServiceFactory


class CodeStarconnectionsService(ServiceFactory[CodeStarconnectionsClient]):
    """
    CodeStarconnections service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codestar_connections/)
    """
