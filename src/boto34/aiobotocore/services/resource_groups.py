"""
Wrapper for aiobotocore ResourceGroups service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_resource_groups/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_resource_groups.client import ResourceGroupsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ResourceGroupsService(ServiceFactory[ResourceGroupsClient]):
    """
    ResourceGroups service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_resource_groups/)
    """
