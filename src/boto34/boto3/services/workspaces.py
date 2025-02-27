"""
Wrapper for boto3 WorkSpaces service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_workspaces/)

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
    # Returns type annotated boto3 WorkSpaces client
    workspaces_client = session.workspaces.client()
    workspaces_client: types_boto3_workspaces.client.WorkSpacesClient
    ```
"""

from __future__ import annotations

from types_boto3_workspaces.client import WorkSpacesClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_workspaces.client import WorkSpacesClient
except ImportError:
    WorkSpacesClient = object  # type: ignore[misc,assignment]


class WorkSpacesService(
    ServiceFactory[WorkSpacesClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "workspaces"
    _SERVICE_PROP = "workspaces"
