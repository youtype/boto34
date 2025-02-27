"""
Wrapper for aiobotocore WorkSpacesThinClient service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_thin_client/)

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
    # Returns type annotated aiobotocore WorkSpacesThinClient client
    async with session.workspaces_thin_client.create_client() as workspaces_thin_client_client:
        workspaces_thin_client_client: (
            types_aiobotocore_workspaces_thin_client.client.WorkSpacesThinClientClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_workspaces_thin_client.client import WorkSpacesThinClientClient

from boto34.aiobotocore.service_factory import ServiceFactory


class WorkSpacesThinClientService(ServiceFactory[WorkSpacesThinClientClient]):
    SERVICE_NAME = "workspaces-thin-client"
    _SERVICE_PROP = "workspaces_thin_client"
