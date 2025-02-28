"""
Wrapper for boto3 CloudFrontKeyValueStore service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudfront_keyvaluestore/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_cloudfront_keyvaluestore.client import CloudFrontKeyValueStoreClient

from boto34.boto3.service_factory import ServiceFactory


class CloudFrontKeyValueStoreService(ServiceFactory[CloudFrontKeyValueStoreClient]):
    """
    CloudFrontKeyValueStore service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudfront_keyvaluestore/)
    """
