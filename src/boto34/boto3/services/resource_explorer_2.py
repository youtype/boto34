"""
Wrapper for boto3 ResourceExplorer service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_resource_explorer_2/)

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
    # Returns type annotated boto3 ResourceExplorer client
    resource_explorer_2_client = session.resource_explorer_2.client()
    resource_explorer_2_client: types_boto3_resource_explorer_2.client.ResourceExplorerClient
    ```
"""

from __future__ import annotations

from types_boto3_resource_explorer_2.client import ResourceExplorerClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_resource_explorer_2.client import ResourceExplorerClient
except ImportError:
    ResourceExplorerClient = object  # type: ignore[misc,assignment]


class ResourceExplorerService(
    ServiceFactory[ResourceExplorerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "resource-explorer-2"
    _SERVICE_PROP = "resource_explorer_2"
