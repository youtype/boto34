"""
Wrapper for aioboto3 MigrationHubConfig service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_migrationhub_config/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_migrationhub_config.client import MigrationHubConfigClient

from boto34.aioboto3.service_factory import ServiceFactory


class MigrationHubConfigService(ServiceFactory[MigrationHubConfigClient]):
    """
    MigrationHubConfig service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_migrationhub_config/)
    """
