"""
Wrapper for aiobotocore MigrationHubConfig service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhub_config/)

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
    # Returns type annotated aiobotocore MigrationHubConfig client
    async with session.migrationhub_config.create_client() as migrationhub_config_client:
        migrationhub_config_client: (
            types_aiobotocore_migrationhub_config.client.MigrationHubConfigClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_migrationhub_config.client import MigrationHubConfigClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_migrationhub_config.client import MigrationHubConfigClient
except ImportError:
    MigrationHubConfigClient = object  # type: ignore[misc,assignment]


class MigrationHubConfigService(
    ServiceFactory[MigrationHubConfigClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "migrationhub-config"
    _SERVICE_PROP = "migrationhub_config"
