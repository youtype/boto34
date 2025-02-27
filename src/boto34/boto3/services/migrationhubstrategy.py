"""
Wrapper for boto3 MigrationHubStrategyRecommendations service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_migrationhubstrategy/)

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
    # Returns type annotated boto3 MigrationHubStrategyRecommendations client
    migrationhubstrategy_client = session.migrationhubstrategy.client()
    migrationhubstrategy_client: (
        types_boto3_migrationhubstrategy.client.MigrationHubStrategyRecommendationsClient
    )
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_migrationhubstrategy.client import MigrationHubStrategyRecommendationsClient
except ImportError:
    MigrationHubStrategyRecommendationsClient = object  # type: ignore[misc,assignment]


class MigrationHubStrategyRecommendationsService(
    ServiceFactory[MigrationHubStrategyRecommendationsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "migrationhubstrategy"
    _SERVICE_PROP = "migrationhubstrategy"
