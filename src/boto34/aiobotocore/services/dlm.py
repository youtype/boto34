"""
Wrapper for aiobotocore DLM service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dlm/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_dlm.client import DLMClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DLMService(ServiceFactory[DLMClient]):
    """
    DLM service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dlm/)
    """
