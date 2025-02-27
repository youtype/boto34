"""
Wrapper for aiobotocore KendraRanking service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/)

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
    # Returns type annotated aiobotocore KendraRanking client
    async with session.kendra_ranking.create_client() as kendra_ranking_client:
        kendra_ranking_client: types_aiobotocore_kendra_ranking.client.KendraRankingClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_kendra_ranking.client import KendraRankingClient
except ImportError:
    KendraRankingClient = object  # type: ignore[misc,assignment]


class KendraRankingService(
    ServiceFactory[KendraRankingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kendra-ranking"
    _SERVICE_PROP = "kendra_ranking"
