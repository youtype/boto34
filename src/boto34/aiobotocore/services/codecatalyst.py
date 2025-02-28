"""
Wrapper for aiobotocore CodeCatalyst service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_codecatalyst.client import CodeCatalystClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CodeCatalystService(ServiceFactory[CodeCatalystClient]):
    """
    CodeCatalyst service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/)
    """
