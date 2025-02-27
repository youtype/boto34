"""
Wrapper for boto3 ElastiCache service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_elasticache/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 ElastiCache client
    elasticache_client = session.elasticache.client()
    elasticache_client: types_boto3_elasticache.client.ElastiCacheClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_elasticache.client import ElastiCacheClient
except ImportError:
    ElastiCacheClient = object  # type: ignore[misc,assignment]


class ElastiCacheService(
    ServiceFactory[ElastiCacheClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "elasticache"
    _SERVICE_PROP = "elasticache"
