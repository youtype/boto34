"""
Wrapper for aioboto3 KendraRanking service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kendra_ranking/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_kendra_ranking.client import KendraRankingClient

from boto34.aioboto3.service_factory import ServiceFactory


class KendraRankingService(ServiceFactory[KendraRankingClient]):
    """
    KendraRanking service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kendra_ranking/)
    """
