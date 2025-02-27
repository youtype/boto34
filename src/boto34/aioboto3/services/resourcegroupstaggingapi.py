"""
Wrapper for aioboto3 ResourceGroupsTaggingAPI service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_resourcegroupstaggingapi/)

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
    # Returns type annotated aioboto3 ResourceGroupsTaggingAPI client
    resourcegroupstaggingapi_client = session.resourcegroupstaggingapi.client()
    resourcegroupstaggingapi_client: (
        types_aiobotocore_resourcegroupstaggingapi.client.ResourceGroupsTaggingAPIClient
    )
    ```
"""

from __future__ import annotations

from types_aiobotocore_resourcegroupstaggingapi.client import ResourceGroupsTaggingAPIClient

from boto34.aioboto3.service_factory import ServiceFactory


class ResourceGroupsTaggingAPIService(ServiceFactory[ResourceGroupsTaggingAPIClient]):
    SERVICE_NAME = "resourcegroupstaggingapi"
    _SERVICE_PROP = "resourcegroupstaggingapi"
