"""
Wrapper for aiobotocore CloudFrontKeyValueStore service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront_keyvaluestore/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cloudfront_keyvaluestore.client import CloudFrontKeyValueStoreClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudFrontKeyValueStoreService(ServiceFactory[CloudFrontKeyValueStoreClient]):
    """
    CloudFrontKeyValueStore service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront_keyvaluestore/)
    """
