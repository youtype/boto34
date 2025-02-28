"""
Wrapper for aioboto3 OpenSearchService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_opensearch/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_opensearch.client import OpenSearchServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class OpenSearchServiceService(ServiceFactory[OpenSearchServiceClient]):
    """
    OpenSearchService service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_opensearch/)
    """
