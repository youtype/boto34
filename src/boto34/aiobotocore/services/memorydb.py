"""
Wrapper for aiobotocore MemoryDB service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_memorydb/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_memorydb.client import MemoryDBClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MemoryDBService(ServiceFactory[MemoryDBClient]):
    """
    MemoryDB service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_memorydb/)
    """
