"""
Wrapper for boto3 MigrationHubConfig service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_migrationhub_config/)

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
    # Returns type annotated boto3 MigrationHubConfig client
    migrationhub_config_client = session.migrationhub_config.client()
    migrationhub_config_client: types_boto3_migrationhub_config.client.MigrationHubConfigClient
    ```
"""

from __future__ import annotations

from types_boto3_migrationhub_config.client import MigrationHubConfigClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_migrationhub_config.client import MigrationHubConfigClient
except ImportError:
    MigrationHubConfigClient = object  # type: ignore[misc,assignment]


class MigrationHubConfigService(
    ServiceFactory[MigrationHubConfigClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "migrationhub-config"
    _SERVICE_PROP = "migrationhub_config"
