"""
Wrapper for aioboto3 ResourceGroups service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_resource_groups/)

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
    # Returns type annotated aioboto3 ResourceGroups client
    resource_groups_client = session.resource_groups.client()
    resource_groups_client: types_aiobotocore_resource_groups.client.ResourceGroupsClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_resource_groups.client import ResourceGroupsClient
except ImportError:
    ResourceGroupsClient = object  # type: ignore[misc,assignment]


class ResourceGroupsService(
    ServiceFactory[ResourceGroupsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "resource-groups"
    _SERVICE_PROP = "resource_groups"
