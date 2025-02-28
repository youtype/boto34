"""
Wrapper for aiobotocore ElastiCache service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elasticache/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_elasticache.client import ElastiCacheClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ElastiCacheService(ServiceFactory[ElastiCacheClient]):
    """
    ElastiCache service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elasticache/)
    """
