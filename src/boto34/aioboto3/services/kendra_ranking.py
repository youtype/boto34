"""
Wrapper for aioboto3 KendraRanking service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kendra_ranking/)

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
    # Returns type annotated aioboto3 KendraRanking client
    kendra_ranking_client = session.kendra_ranking.client()
    kendra_ranking_client: types_aiobotocore_kendra_ranking.client.KendraRankingClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_kendra_ranking.client import KendraRankingClient

from boto34.aioboto3.service_factory import ServiceFactory


class KendraRankingService(ServiceFactory[KendraRankingClient]):
    SERVICE_NAME = "kendra-ranking"
    _SERVICE_PROP = "kendra_ranking"
