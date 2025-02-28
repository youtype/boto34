"""
Wrapper for aioboto3 MainframeModernization service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_m2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_m2.client import MainframeModernizationClient

from boto34.aioboto3.service_factory import ServiceFactory


class MainframeModernizationService(ServiceFactory[MainframeModernizationClient]):
    """
    MainframeModernization service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_m2/)
    """
