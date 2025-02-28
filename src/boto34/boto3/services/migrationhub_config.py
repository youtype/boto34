"""
Wrapper for boto3 MigrationHubConfig service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_migrationhub_config/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_migrationhub_config.client import MigrationHubConfigClient

from boto34.boto3.service_factory import ServiceFactory


class MigrationHubConfigService(ServiceFactory[MigrationHubConfigClient]):
    """
    MigrationHubConfig service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_migrationhub_config/)
    """
