"""
Wrapper for aioboto3 DocDBElastic service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_docdb_elastic/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_docdb_elastic.client import DocDBElasticClient

from boto34.aioboto3.service_factory import ServiceFactory


class DocDBElasticService(ServiceFactory[DocDBElasticClient]):
    """
    DocDBElastic service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_docdb_elastic/)
    """
