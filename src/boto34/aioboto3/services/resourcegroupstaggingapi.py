"""
Wrapper for aioboto3 ResourceGroupsTaggingAPI service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_resourcegroupstaggingapi/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_resourcegroupstaggingapi.client import ResourceGroupsTaggingAPIClient

from boto34.aioboto3.service_factory import ServiceFactory


class ResourceGroupsTaggingAPIService(ServiceFactory[ResourceGroupsTaggingAPIClient]):
    """
    ResourceGroupsTaggingAPI service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_resourcegroupstaggingapi/)
    """
