"""
Wrapper for aiobotocore ServerlessApplicationRepository service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_serverlessrepo/)

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
    # Returns type annotated aiobotocore ServerlessApplicationRepository client
    async with session.serverlessrepo.create_client() as serverlessrepo_client:
        serverlessrepo_client: (
            types_aiobotocore_serverlessrepo.client.ServerlessApplicationRepositoryClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_serverlessrepo.client import ServerlessApplicationRepositoryClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ServerlessApplicationRepositoryService(ServiceFactory[ServerlessApplicationRepositoryClient]):
    SERVICE_NAME = "serverlessrepo"
    _SERVICE_PROP = "serverlessrepo"
