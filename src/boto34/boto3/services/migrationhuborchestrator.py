"""
Wrapper for boto3 MigrationHubOrchestrator service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_migrationhuborchestrator/)

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
    # Returns type annotated boto3 MigrationHubOrchestrator client
    migrationhuborchestrator_client = session.migrationhuborchestrator.client()
    migrationhuborchestrator_client: (
        types_boto3_migrationhuborchestrator.client.MigrationHubOrchestratorClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_migrationhuborchestrator.client import MigrationHubOrchestratorClient

from boto34.boto3.service_factory import ServiceFactory


class MigrationHubOrchestratorService(ServiceFactory[MigrationHubOrchestratorClient]):
    SERVICE_NAME = "migrationhuborchestrator"
    _SERVICE_PROP = "migrationhuborchestrator"
