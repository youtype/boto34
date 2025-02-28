"""
Wrapper for boto3 AccessAnalyzer service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_accessanalyzer/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_accessanalyzer.client import AccessAnalyzerClient

from boto34.boto3.service_factory import ServiceFactory


class AccessAnalyzerService(ServiceFactory[AccessAnalyzerClient]):
    """
    AccessAnalyzer service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_accessanalyzer/)
    """
