"""
Wrapper for aioboto3 MigrationHubStrategyRecommendations service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_migrationhubstrategy/)

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
    # Returns type annotated aioboto3 MigrationHubStrategyRecommendations client
    migrationhubstrategy_client = session.migrationhubstrategy.client()
    migrationhubstrategy_client: (
        types_aiobotocore_migrationhubstrategy.client.MigrationHubStrategyRecommendationsClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

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
