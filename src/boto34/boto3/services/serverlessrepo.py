"""
Wrapper for boto3 ServerlessApplicationRepository service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_serverlessrepo/)

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
    # Returns type annotated boto3 ServerlessApplicationRepository client
    serverlessrepo_client = session.serverlessrepo.client()
    serverlessrepo_client: types_boto3_serverlessrepo.client.ServerlessApplicationRepositoryClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_serverlessrepo.client import ServerlessApplicationRepositoryClient
except ImportError:
    ServerlessApplicationRepositoryClient = object  # type: ignore[misc,assignment]


class ServerlessApplicationRepositoryService(
    ServiceFactory[ServerlessApplicationRepositoryClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "serverlessrepo"
    _SERVICE_PROP = "serverlessrepo"
