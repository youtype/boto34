"""
Wrapper for aiobotocore ResourceGroupsTaggingAPI service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_resourcegroupstaggingapi/)

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
    # Returns type annotated aiobotocore ResourceGroupsTaggingAPI client
    async with session.resourcegroupstaggingapi.create_client() as resourcegroupstaggingapi_client:
        resourcegroupstaggingapi_client: (
            types_aiobotocore_resourcegroupstaggingapi.client.ResourceGroupsTaggingAPIClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_resourcegroupstaggingapi.client import ResourceGroupsTaggingAPIClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_resourcegroupstaggingapi.client import ResourceGroupsTaggingAPIClient
except ImportError:
    ResourceGroupsTaggingAPIClient = object  # type: ignore[misc,assignment]


class ResourceGroupsTaggingAPIService(
    ServiceFactory[ResourceGroupsTaggingAPIClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "resourcegroupstaggingapi"
    _SERVICE_PROP = "resourcegroupstaggingapi"
