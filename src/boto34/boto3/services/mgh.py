"""
Wrapper for boto3 MigrationHub service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mgh/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_mgh.client import MigrationHubClient

from boto34.boto3.service_factory import ServiceFactory


class MigrationHubService(ServiceFactory[MigrationHubClient]):
    """
    MigrationHub service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mgh/)
    """
