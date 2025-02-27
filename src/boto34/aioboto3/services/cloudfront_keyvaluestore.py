"""
Wrapper for aioboto3 CloudFrontKeyValueStore service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudfront_keyvaluestore/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 CloudFrontKeyValueStore client
    cloudfront_keyvaluestore_client = session.cloudfront_keyvaluestore.client()
    cloudfront_keyvaluestore_client: (
        types_aiobotocore_cloudfront_keyvaluestore.client.CloudFrontKeyValueStoreClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_cloudfront_keyvaluestore.client import CloudFrontKeyValueStoreClient
except ImportError:
    CloudFrontKeyValueStoreClient = object  # type: ignore[misc,assignment]


class CloudFrontKeyValueStoreService(
    ServiceFactory[CloudFrontKeyValueStoreClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloudfront-keyvaluestore"
    _SERVICE_PROP = "cloudfront_keyvaluestore"
