"""
Wrapper for boto3 MigrationHubOrchestrator service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_migrationhuborchestrator/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_migrationhuborchestrator.client import MigrationHubOrchestratorClient

from boto34.boto3.service_factory import ServiceFactory


class MigrationHubOrchestratorService(ServiceFactory[MigrationHubOrchestratorClient]):
    """
    MigrationHubOrchestrator service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_migrationhuborchestrator/)
    """
