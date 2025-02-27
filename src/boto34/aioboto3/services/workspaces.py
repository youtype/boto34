"""
Wrapper for aioboto3 WorkSpaces service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_workspaces/)

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
    # Returns type annotated aioboto3 WorkSpaces client
    workspaces_client = session.workspaces.client()
    workspaces_client: types_aiobotocore_workspaces.client.WorkSpacesClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_workspaces.client import WorkSpacesClient
except ImportError:
    WorkSpacesClient = object  # type: ignore[misc,assignment]


class WorkSpacesService(
    ServiceFactory[WorkSpacesClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "workspaces"
    _SERVICE_PROP = "workspaces"
