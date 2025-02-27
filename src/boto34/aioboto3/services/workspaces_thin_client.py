"""
Wrapper for aioboto3 WorkSpacesThinClient service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_workspaces_thin_client/)

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
    # Returns type annotated aioboto3 WorkSpacesThinClient client
    workspaces_thin_client_client = session.workspaces_thin_client.client()
    workspaces_thin_client_client: (
        types_aiobotocore_workspaces_thin_client.client.WorkSpacesThinClientClient
    )
    ```
"""

from __future__ import annotations

from types_aiobotocore_workspaces_thin_client.client import WorkSpacesThinClientClient

from boto34.aioboto3.service_factory import ServiceFactory


class WorkSpacesThinClientService(ServiceFactory[WorkSpacesThinClientClient]):
    SERVICE_NAME = "workspaces-thin-client"
    _SERVICE_PROP = "workspaces_thin_client"
