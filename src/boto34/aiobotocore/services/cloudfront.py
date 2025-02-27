"""
Wrapper for aiobotocore CloudFront service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/)

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
    # Returns type annotated aiobotocore CloudFront client
    async with session.cloudfront.create_client() as cloudfront_client:
        cloudfront_client: types_aiobotocore_cloudfront.client.CloudFrontClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_cloudfront.client import CloudFrontClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudFrontService(ServiceFactory[CloudFrontClient]):
    SERVICE_NAME = "cloudfront"
    _SERVICE_PROP = "cloudfront"
