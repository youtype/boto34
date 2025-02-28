"""
Wrapper for aiobotocore CloudSearch service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudsearch/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cloudsearch.client import CloudSearchClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudSearchService(ServiceFactory[CloudSearchClient]):
    """
    CloudSearch service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudsearch/)
    """
