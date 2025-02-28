"""
Wrapper for aioboto3 MigrationHubRefactorSpaces service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_migration_hub_refactor_spaces/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_migration_hub_refactor_spaces.client import MigrationHubRefactorSpacesClient

from boto34.aioboto3.service_factory import ServiceFactory


class MigrationHubRefactorSpacesService(ServiceFactory[MigrationHubRefactorSpacesClient]):
    """
    MigrationHubRefactorSpaces service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_migration_hub_refactor_spaces/)
    """
