"""
Wrapper for aiobotocore MigrationHubStrategyRecommendations service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhubstrategy/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_migrationhubstrategy.client import MigrationHubStrategyRecommendationsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MigrationHubStrategyRecommendationsService(
    ServiceFactory[MigrationHubStrategyRecommendationsClient]
):
    """
    MigrationHubStrategyRecommendations service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhubstrategy/)
    """
