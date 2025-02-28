"""
Wrapper for aiobotocore AccessAnalyzer service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_accessanalyzer/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_accessanalyzer.client import AccessAnalyzerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AccessAnalyzerService(ServiceFactory[AccessAnalyzerClient]):
    """
    AccessAnalyzer service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_accessanalyzer/)
    """
