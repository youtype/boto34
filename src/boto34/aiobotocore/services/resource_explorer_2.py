"""
Wrapper for aiobotocore ResourceExplorer service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_resource_explorer_2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_resource_explorer_2.client import ResourceExplorerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ResourceExplorerService(ServiceFactory[ResourceExplorerClient]):
    """
    ResourceExplorer service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_resource_explorer_2/)
    """
