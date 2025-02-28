"""
Wrapper for aiobotocore CloudWatchRUM service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_rum.client import CloudWatchRUMClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudWatchRUMService(ServiceFactory[CloudWatchRUMClient]):
    """
    CloudWatchRUM service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/)
    """
