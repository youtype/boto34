"""
Wrapper for boto3 ServerlessApplicationRepository service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_serverlessrepo/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_serverlessrepo.client import ServerlessApplicationRepositoryClient

from boto34.boto3.service_factory import ServiceFactory


class ServerlessApplicationRepositoryService(ServiceFactory[ServerlessApplicationRepositoryClient]):
    """
    ServerlessApplicationRepository service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_serverlessrepo/)
    """
