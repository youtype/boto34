"""
Wrapper for aiobotocore CloudFrontKeyValueStore service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront_keyvaluestore/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore CloudFrontKeyValueStore client
    async with session.cloudfront_keyvaluestore.create_client() as cloudfront_keyvaluestore_client:
        cloudfront_keyvaluestore_client: (
            types_aiobotocore_cloudfront_keyvaluestore.client.CloudFrontKeyValueStoreClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_cloudfront_keyvaluestore.client import CloudFrontKeyValueStoreClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudFrontKeyValueStoreService(ServiceFactory[CloudFrontKeyValueStoreClient]):
    SERVICE_NAME = "cloudfront-keyvaluestore"
    _SERVICE_PROP = "cloudfront_keyvaluestore"
