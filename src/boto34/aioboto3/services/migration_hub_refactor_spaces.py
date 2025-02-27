"""
Wrapper for aioboto3 MigrationHubRefactorSpaces service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_migration_hub_refactor_spaces/)

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
    # Returns type annotated aioboto3 MigrationHubRefactorSpaces client
    migration_hub_refactor_spaces_client = session.migration_hub_refactor_spaces.client()
    migration_hub_refactor_spaces_client: (
        types_aiobotocore_migration_hub_refactor_spaces.client.MigrationHubRefactorSpacesClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_migration_hub_refactor_spaces.client import (
        MigrationHubRefactorSpacesClient,
    )
except ImportError:
    MigrationHubRefactorSpacesClient = object  # type: ignore[misc,assignment]


class MigrationHubRefactorSpacesService(
    ServiceFactory[MigrationHubRefactorSpacesClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "migration-hub-refactor-spaces"
    _SERVICE_PROP = "migration_hub_refactor_spaces"
