"""
Wrapper for aiobotocore RAM service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ram/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ram.client import RAMClient

from boto34.aiobotocore.service_factory import ServiceFactory


class RAMService(ServiceFactory[RAMClient]):
    """
    RAM service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ram/)
    """
