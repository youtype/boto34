"""
Wrapper for aiobotocore KendraRanking service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_kendra_ranking.client import KendraRankingClient

from boto34.aiobotocore.service_factory import ServiceFactory


class KendraRankingService(ServiceFactory[KendraRankingClient]):
    """
    KendraRanking service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/)
    """
