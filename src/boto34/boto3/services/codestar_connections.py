"""
Wrapper for boto3 CodeStarconnections service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_connections/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_codestar_connections.client import CodeStarconnectionsClient

from boto34.boto3.service_factory import ServiceFactory


class CodeStarconnectionsService(ServiceFactory[CodeStarconnectionsClient]):
    """
    CodeStarconnections service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_connections/)
    """
