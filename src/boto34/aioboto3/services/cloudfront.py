"""
Wrapper for aioboto3 CloudFront service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudfront/)

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
    # Returns type annotated aioboto3 CloudFront client
    cloudfront_client = session.cloudfront.client()
    cloudfront_client: types_aiobotocore_cloudfront.client.CloudFrontClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_cloudfront.client import CloudFrontClient

from boto34.aioboto3.service_factory import ServiceFactory


class CloudFrontService(ServiceFactory[CloudFrontClient]):
    SERVICE_NAME = "cloudfront"
    _SERVICE_PROP = "cloudfront"
