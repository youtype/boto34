"""
Wrapper for aiobotocore MigrationHubOrchestrator service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_migrationhuborchestrator.client import MigrationHubOrchestratorClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MigrationHubOrchestratorService(ServiceFactory[MigrationHubOrchestratorClient]):
    """
    MigrationHubOrchestrator service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/)
    """
