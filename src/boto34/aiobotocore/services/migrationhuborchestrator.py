"""
Wrapper for aiobotocore MigrationHubOrchestrator service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/)

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
    # Returns type annotated aiobotocore MigrationHubOrchestrator client
    async with session.migrationhuborchestrator.create_client() as migrationhuborchestrator_client:
        migrationhuborchestrator_client: (
            types_aiobotocore_migrationhuborchestrator.client.MigrationHubOrchestratorClient
        )
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_migrationhuborchestrator.client import MigrationHubOrchestratorClient
except ImportError:
    MigrationHubOrchestratorClient = object  # type: ignore[misc,assignment]


class MigrationHubOrchestratorService(
    ServiceFactory[MigrationHubOrchestratorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "migrationhuborchestrator"
    _SERVICE_PROP = "migrationhuborchestrator"
