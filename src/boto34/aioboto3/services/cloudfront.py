"""
Wrapper for aioboto3 CloudFront service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudfront/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cloudfront.client import CloudFrontClient

from boto34.aioboto3.service_factory import ServiceFactory


class CloudFrontService(ServiceFactory[CloudFrontClient]):
    """
    CloudFront service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudfront/)
    """
