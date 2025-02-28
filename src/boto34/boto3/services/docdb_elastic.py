"""
Wrapper for boto3 DocDBElastic service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_docdb_elastic/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_docdb_elastic.client import DocDBElasticClient

from boto34.boto3.service_factory import ServiceFactory


class DocDBElasticService(ServiceFactory[DocDBElasticClient]):
    """
    DocDBElastic service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_docdb_elastic/)
    """
