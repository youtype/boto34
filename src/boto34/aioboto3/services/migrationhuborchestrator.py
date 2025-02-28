"""
Wrapper for aioboto3 MigrationHubOrchestrator service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_migrationhuborchestrator/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_migrationhuborchestrator.client import MigrationHubOrchestratorClient

from boto34.aioboto3.service_factory import ServiceFactory


class MigrationHubOrchestratorService(ServiceFactory[MigrationHubOrchestratorClient]):
    """
    MigrationHubOrchestrator service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_migrationhuborchestrator/)
    """
