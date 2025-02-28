"""
Wrapper for boto3 OpenSearchService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_opensearch/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_opensearch.client import OpenSearchServiceClient

from boto34.boto3.service_factory import ServiceFactory


class OpenSearchServiceService(ServiceFactory[OpenSearchServiceClient]):
    """
    OpenSearchService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_opensearch/)
    """
