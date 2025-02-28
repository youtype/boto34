"""
Wrapper for aiobotocore CloudDirectory service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_clouddirectory/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_clouddirectory.client import CloudDirectoryClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudDirectoryService(ServiceFactory[CloudDirectoryClient]):
    """
    CloudDirectory service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_clouddirectory/)
    """
