"""
Wrapper for boto3 CloudFront service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudfront/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_cloudfront.client import CloudFrontClient

from boto34.boto3.service_factory import ServiceFactory


class CloudFrontService(ServiceFactory[CloudFrontClient]):
    """
    CloudFront service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudfront/)
    """
