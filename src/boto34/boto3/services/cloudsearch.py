"""
Wrapper for boto3 CloudSearch service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudsearch/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_cloudsearch.client import CloudSearchClient

from boto34.boto3.service_factory import ServiceFactory


class CloudSearchService(ServiceFactory[CloudSearchClient]):
    """
    CloudSearch service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudsearch/)
    """
