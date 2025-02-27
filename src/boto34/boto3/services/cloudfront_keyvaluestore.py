"""
Wrapper for boto3 CloudFrontKeyValueStore service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudfront_keyvaluestore/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 CloudFrontKeyValueStore client
    cloudfront_keyvaluestore_client = session.cloudfront_keyvaluestore.client()
    cloudfront_keyvaluestore_client: (
        types_boto3_cloudfront_keyvaluestore.client.CloudFrontKeyValueStoreClient
    )
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_cloudfront_keyvaluestore.client import CloudFrontKeyValueStoreClient
except ImportError:
    CloudFrontKeyValueStoreClient = object  # type: ignore[misc,assignment]


class CloudFrontKeyValueStoreService(
    ServiceFactory[CloudFrontKeyValueStoreClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloudfront-keyvaluestore"
    _SERVICE_PROP = "cloudfront_keyvaluestore"
