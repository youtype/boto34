"""
Wrapper for boto3 MainframeModernization service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_m2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_m2.client import MainframeModernizationClient

from boto34.boto3.service_factory import ServiceFactory


class MainframeModernizationService(ServiceFactory[MainframeModernizationClient]):
    """
    MainframeModernization service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_m2/)
    """
