"""
Wrapper for aiobotocore WorkSpaces service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces/)

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
    # Returns type annotated aiobotocore WorkSpaces client
    async with session.workspaces.create_client() as workspaces_client:
        workspaces_client: types_aiobotocore_workspaces.client.WorkSpacesClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_workspaces.client import WorkSpacesClient

from boto34.aiobotocore.service_factory import ServiceFactory


class WorkSpacesService(ServiceFactory[WorkSpacesClient]):
    SERVICE_NAME = "workspaces"
    _SERVICE_PROP = "workspaces"
