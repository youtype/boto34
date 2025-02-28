"""
Wrapper for aioboto3 ElasticsearchService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_es/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_es.client import ElasticsearchServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class ElasticsearchServiceService(ServiceFactory[ElasticsearchServiceClient]):
    """
    ElasticsearchService service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_es/)
    """
