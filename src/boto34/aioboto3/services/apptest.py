"""
Wrapper for aioboto3 MainframeModernizationApplicationTesting service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_apptest/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_apptest.client import MainframeModernizationApplicationTestingClient

from boto34.aioboto3.service_factory import ServiceFactory


class MainframeModernizationApplicationTestingService(
    ServiceFactory[MainframeModernizationApplicationTestingClient]
):
    """
    MainframeModernizationApplicationTesting service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_apptest/)
    """
