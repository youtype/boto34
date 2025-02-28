"""
Wrapper for boto3 CloudWatch service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudwatch/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_cloudwatch.client import CloudWatchClient
from types_boto3_cloudwatch.service_resource import CloudWatchServiceResource

from boto34.boto3.service_factory import ServiceResourceFactory


class CloudWatchService(ServiceResourceFactory[CloudWatchClient, CloudWatchServiceResource]):
    """
    CloudWatch service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudwatch/)
    """
