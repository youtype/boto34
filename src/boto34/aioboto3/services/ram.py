"""
Wrapper for aioboto3 RAM service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ram/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ram.client import RAMClient

from boto34.aioboto3.service_factory import ServiceFactory


class RAMService(ServiceFactory[RAMClient]):
    """
    RAM service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ram/)
    """
