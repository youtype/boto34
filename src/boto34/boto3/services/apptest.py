"""
Wrapper for boto3 MainframeModernizationApplicationTesting service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_apptest.client import MainframeModernizationApplicationTestingClient

from boto34.boto3.service_factory import ServiceFactory


class MainframeModernizationApplicationTestingService(
    ServiceFactory[MainframeModernizationApplicationTestingClient]
):
    """
    MainframeModernizationApplicationTesting service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/)
    """
