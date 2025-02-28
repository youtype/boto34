"""
Wrapper for aiobotocore DirectoryService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ds/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ds.client import DirectoryServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DirectoryServiceService(ServiceFactory[DirectoryServiceClient]):
    """
    DirectoryService service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ds/)
    """
