"""
Wrapper for boto3 ElastiCache service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_elasticache/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_elasticache.client import ElastiCacheClient

from boto34.boto3.service_factory import ServiceFactory


class ElastiCacheService(ServiceFactory[ElastiCacheClient]):
    """
    ElastiCache service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_elasticache/)
    """
