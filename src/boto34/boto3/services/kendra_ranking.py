"""
Wrapper for boto3 KendraRanking service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kendra_ranking/)

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
    # Returns type annotated boto3 KendraRanking client
    kendra_ranking_client = session.kendra_ranking.client()
    kendra_ranking_client: types_boto3_kendra_ranking.client.KendraRankingClient
    ```
"""

from __future__ import annotations

from types_boto3_kendra_ranking.client import KendraRankingClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_kendra_ranking.client import KendraRankingClient
except ImportError:
    KendraRankingClient = object  # type: ignore[misc,assignment]


class KendraRankingService(
    ServiceFactory[KendraRankingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kendra-ranking"
    _SERVICE_PROP = "kendra_ranking"
