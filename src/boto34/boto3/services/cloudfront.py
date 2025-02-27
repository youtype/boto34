"""
Wrapper for boto3 CloudFront service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudfront/)

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
    # Returns type annotated boto3 CloudFront client
    cloudfront_client = session.cloudfront.client()
    cloudfront_client: types_boto3_cloudfront.client.CloudFrontClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_cloudfront.client import CloudFrontClient
except ImportError:
    CloudFrontClient = object  # type: ignore[misc,assignment]


class CloudFrontService(
    ServiceFactory[CloudFrontClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloudfront"
    _SERVICE_PROP = "cloudfront"
