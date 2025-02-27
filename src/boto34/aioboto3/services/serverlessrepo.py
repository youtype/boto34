"""
Wrapper for aioboto3 ServerlessApplicationRepository service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_serverlessrepo/)

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
    # Returns type annotated aioboto3 ServerlessApplicationRepository client
    serverlessrepo_client = session.serverlessrepo.client()
    serverlessrepo_client: types_aiobotocore_serverlessrepo.client.ServerlessApplicationRepositoryClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_serverlessrepo.client import ServerlessApplicationRepositoryClient

from boto34.aioboto3.service_factory import ServiceFactory


class ServerlessApplicationRepositoryService(ServiceFactory[ServerlessApplicationRepositoryClient]):
    SERVICE_NAME = "serverlessrepo"
    _SERVICE_PROP = "serverlessrepo"
