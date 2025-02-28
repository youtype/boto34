"""
Wrapper for boto3 ElasticsearchService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_es/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_es.client import ElasticsearchServiceClient

from boto34.boto3.service_factory import ServiceFactory


class ElasticsearchServiceService(ServiceFactory[ElasticsearchServiceClient]):
    """
    ElasticsearchService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_es/)
    """
