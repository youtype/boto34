"""
Wrapper for aiobotocore ElastiCache service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elasticache/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore ElastiCache client
    async with session.elasticache.create_client() as elasticache_client:
        elasticache_client: types_aiobotocore_elasticache.client.ElastiCacheClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_elasticache.client import ElastiCacheClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ElastiCacheService(ServiceFactory[ElastiCacheClient]):
    SERVICE_NAME = "elasticache"
    _SERVICE_PROP = "elasticache"
