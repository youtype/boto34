"""
Wrapper for aiobotocore MigrationHubStrategyRecommendations service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhubstrategy/)

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
    # Returns type annotated aiobotocore MigrationHubStrategyRecommendations client
    async with session.migrationhubstrategy.create_client() as migrationhubstrategy_client:
        migrationhubstrategy_client: (
            types_aiobotocore_migrationhubstrategy.client.MigrationHubStrategyRecommendationsClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_migrationhubstrategy.client import MigrationHubStrategyRecommendationsClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_migrationhubstrategy.client import (
        MigrationHubStrategyRecommendationsClient,
    )
except ImportError:
    MigrationHubStrategyRecommendationsClient = object  # type: ignore[misc,assignment]


class MigrationHubStrategyRecommendationsService(
    ServiceFactory[MigrationHubStrategyRecommendationsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "migrationhubstrategy"
    _SERVICE_PROP = "migrationhubstrategy"
