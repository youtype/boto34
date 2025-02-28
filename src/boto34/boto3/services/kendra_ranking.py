"""
Wrapper for boto3 KendraRanking service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kendra_ranking/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_kendra_ranking.client import KendraRankingClient

from boto34.boto3.service_factory import ServiceFactory


class KendraRankingService(ServiceFactory[KendraRankingClient]):
    """
    KendraRanking service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kendra_ranking/)
    """
