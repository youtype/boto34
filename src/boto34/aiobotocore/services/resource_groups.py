"""
Wrapper for aiobotocore ResourceGroups service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_resource_groups/)

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
    # Returns type annotated aiobotocore ResourceGroups client
    async with session.resource_groups.create_client() as resource_groups_client:
        resource_groups_client: types_aiobotocore_resource_groups.client.ResourceGroupsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_resource_groups.client import ResourceGroupsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ResourceGroupsService(ServiceFactory[ResourceGroupsClient]):
    SERVICE_NAME = "resource-groups"
    _SERVICE_PROP = "resource_groups"
