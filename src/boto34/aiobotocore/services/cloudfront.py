"""
Wrapper for aiobotocore CloudFront service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cloudfront.client import CloudFrontClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudFrontService(ServiceFactory[CloudFrontClient]):
    """
    CloudFront service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/)
    """
