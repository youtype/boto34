"""
Wrapper for boto3 CodeCatalyst service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codecatalyst/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_codecatalyst.client import CodeCatalystClient

from boto34.boto3.service_factory import ServiceFactory


class CodeCatalystService(ServiceFactory[CodeCatalystClient]):
    """
    CodeCatalyst service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codecatalyst/)
    """
