"""
Wrapper for aioboto3 MigrationHubConfig service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_migrationhub_config/)

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
    # Returns type annotated aioboto3 MigrationHubConfig client
    migrationhub_config_client = session.migrationhub_config.client()
    migrationhub_config_client: types_aiobotocore_migrationhub_config.client.MigrationHubConfigClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_migrationhub_config.client import MigrationHubConfigClient
except ImportError:
    MigrationHubConfigClient = object  # type: ignore[misc,assignment]


class MigrationHubConfigService(
    ServiceFactory[MigrationHubConfigClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "migrationhub-config"
    _SERVICE_PROP = "migrationhub_config"
