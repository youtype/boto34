"""
Wrapper for boto3 MigrationHubRefactorSpaces service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_migration_hub_refactor_spaces/)

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
    # Returns type annotated boto3 MigrationHubRefactorSpaces client
    migration_hub_refactor_spaces_client = session.migration_hub_refactor_spaces.client()
    migration_hub_refactor_spaces_client: (
        types_boto3_migration_hub_refactor_spaces.client.MigrationHubRefactorSpacesClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_migration_hub_refactor_spaces.client import MigrationHubRefactorSpacesClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_migration_hub_refactor_spaces.client import MigrationHubRefactorSpacesClient
except ImportError:
    MigrationHubRefactorSpacesClient = object  # type: ignore[misc,assignment]


class MigrationHubRefactorSpacesService(
    ServiceFactory[MigrationHubRefactorSpacesClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "migration-hub-refactor-spaces"
    _SERVICE_PROP = "migration_hub_refactor_spaces"
