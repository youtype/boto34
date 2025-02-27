"""
Wrapper for aiobotocore MigrationHubRefactorSpaces service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migration_hub_refactor_spaces/)

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
    # Returns type annotated aiobotocore MigrationHubRefactorSpaces client
    async with (
        session.migration_hub_refactor_spaces.create_client()
    ) as migration_hub_refactor_spaces_client:
        migration_hub_refactor_spaces_client: (
            types_aiobotocore_migration_hub_refactor_spaces.client.MigrationHubRefactorSpacesClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_migration_hub_refactor_spaces.client import MigrationHubRefactorSpacesClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MigrationHubRefactorSpacesService(ServiceFactory[MigrationHubRefactorSpacesClient]):
    SERVICE_NAME = "migration-hub-refactor-spaces"
    _SERVICE_PROP = "migration_hub_refactor_spaces"
