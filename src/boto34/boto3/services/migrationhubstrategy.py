"""
Wrapper for boto3 MigrationHubStrategyRecommendations service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_migrationhubstrategy/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_migrationhubstrategy.client import MigrationHubStrategyRecommendationsClient

from boto34.boto3.service_factory import ServiceFactory


class MigrationHubStrategyRecommendationsService(
    ServiceFactory[MigrationHubStrategyRecommendationsClient]
):
    """
    MigrationHubStrategyRecommendations service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_migrationhubstrategy/)
    """
