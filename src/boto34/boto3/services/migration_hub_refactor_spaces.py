"""
Wrapper for boto3 MigrationHubRefactorSpaces service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_migration_hub_refactor_spaces/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_migration_hub_refactor_spaces.client import MigrationHubRefactorSpacesClient

from boto34.boto3.service_factory import ServiceFactory


class MigrationHubRefactorSpacesService(ServiceFactory[MigrationHubRefactorSpacesClient]):
    """
    MigrationHubRefactorSpaces service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_migration_hub_refactor_spaces/)
    """
