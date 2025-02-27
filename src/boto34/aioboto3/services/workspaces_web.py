"""
Wrapper for aioboto3 WorkSpacesWeb service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_workspaces_web/)

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
    # Returns type annotated aioboto3 WorkSpacesWeb client
    workspaces_web_client = session.workspaces_web.client()
    workspaces_web_client: types_aiobotocore_workspaces_web.client.WorkSpacesWebClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_workspaces_web.client import WorkSpacesWebClient
except ImportError:
    WorkSpacesWebClient = object  # type: ignore[misc,assignment]


class WorkSpacesWebService(
    ServiceFactory[WorkSpacesWebClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "workspaces-web"
    _SERVICE_PROP = "workspaces_web"
