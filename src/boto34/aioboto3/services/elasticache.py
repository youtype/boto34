"""
Wrapper for aioboto3 ElastiCache service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_elasticache/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 ElastiCache client
    elasticache_client = session.elasticache.client()
    elasticache_client: types_aiobotocore_elasticache.client.ElastiCacheClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_elasticache.client import ElastiCacheClient

from boto34.aioboto3.service_factory import ServiceFactory


class ElastiCacheService(ServiceFactory[ElastiCacheClient]):
    SERVICE_NAME = "elasticache"
    _SERVICE_PROP = "elasticache"
