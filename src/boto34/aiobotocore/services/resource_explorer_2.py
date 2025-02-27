"""
Wrapper for aiobotocore ResourceExplorer service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_resource_explorer_2/)

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
    # Returns type annotated aiobotocore ResourceExplorer client
    async with session.resource_explorer_2.create_client() as resource_explorer_2_client:
        resource_explorer_2_client: types_aiobotocore_resource_explorer_2.client.ResourceExplorerClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_resource_explorer_2.client import ResourceExplorerClient
except ImportError:
    ResourceExplorerClient = object  # type: ignore[misc,assignment]


class ResourceExplorerService(
    ServiceFactory[ResourceExplorerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "resource-explorer-2"
    _SERVICE_PROP = "resource_explorer_2"
