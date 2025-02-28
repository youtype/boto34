"""
Wrapper for boto3 OpenSearchServiceServerless service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_opensearchserverless/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_opensearchserverless.client import OpenSearchServiceServerlessClient

from boto34.boto3.service_factory import ServiceFactory


class OpenSearchServiceServerlessService(ServiceFactory[OpenSearchServiceServerlessClient]):
    """
    OpenSearchServiceServerless service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_opensearchserverless/)
    """
