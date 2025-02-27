"""
Wrapper for aiobotocore WorkSpacesWeb service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/)

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
    # Returns type annotated aiobotocore WorkSpacesWeb client
    async with session.workspaces_web.create_client() as workspaces_web_client:
        workspaces_web_client: types_aiobotocore_workspaces_web.client.WorkSpacesWebClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_workspaces_web.client import WorkSpacesWebClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_workspaces_web.client import WorkSpacesWebClient
except ImportError:
    WorkSpacesWebClient = object  # type: ignore[misc,assignment]


class WorkSpacesWebService(
    ServiceFactory[WorkSpacesWebClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "workspaces-web"
    _SERVICE_PROP = "workspaces_web"
