"""
Wrapper for boto3 CloudTrail service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudtrail/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_cloudtrail.client import CloudTrailClient

from boto34.boto3.service_factory import ServiceFactory


class CloudTrailService(ServiceFactory[CloudTrailClient]):
    """
    CloudTrail service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudtrail/)
    """
