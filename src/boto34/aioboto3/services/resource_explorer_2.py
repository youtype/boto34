"""
Wrapper for aioboto3 ResourceExplorer service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_resource_explorer_2/)

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
    # Returns type annotated aioboto3 ResourceExplorer client
    resource_explorer_2_client = session.resource_explorer_2.client()
    resource_explorer_2_client: types_aiobotocore_resource_explorer_2.client.ResourceExplorerClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_resource_explorer_2.client import ResourceExplorerClient
except ImportError:
    ResourceExplorerClient = object  # type: ignore[misc,assignment]


class ResourceExplorerService(
    ServiceFactory[ResourceExplorerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "resource-explorer-2"
    _SERVICE_PROP = "resource_explorer_2"
