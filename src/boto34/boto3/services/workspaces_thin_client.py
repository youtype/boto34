"""
Wrapper for boto3 WorkSpacesThinClient service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_workspaces_thin_client/)

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
    # Returns type annotated boto3 WorkSpacesThinClient client
    workspaces_thin_client_client = session.workspaces_thin_client.client()
    workspaces_thin_client_client: types_boto3_workspaces_thin_client.client.WorkSpacesThinClientClient
    ```
"""

from __future__ import annotations

from types_boto3_workspaces_thin_client.client import WorkSpacesThinClientClient

from boto34.boto3.service_factory import ServiceFactory


class WorkSpacesThinClientService(ServiceFactory[WorkSpacesThinClientClient]):
    SERVICE_NAME = "workspaces-thin-client"
    _SERVICE_PROP = "workspaces_thin_client"
