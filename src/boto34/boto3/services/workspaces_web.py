"""
Wrapper for boto3 WorkSpacesWeb service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_workspaces_web/)

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
    # Returns type annotated boto3 WorkSpacesWeb client
    workspaces_web_client = session.workspaces_web.client()
    workspaces_web_client: types_boto3_workspaces_web.client.WorkSpacesWebClient
    ```
"""

from __future__ import annotations

from types_boto3_workspaces_web.client import WorkSpacesWebClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_workspaces_web.client import WorkSpacesWebClient
except ImportError:
    WorkSpacesWebClient = object  # type: ignore[misc,assignment]


class WorkSpacesWebService(
    ServiceFactory[WorkSpacesWebClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "workspaces-web"
    _SERVICE_PROP = "workspaces_web"
