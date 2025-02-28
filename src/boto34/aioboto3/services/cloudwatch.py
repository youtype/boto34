"""
Wrapper for aioboto3 CloudWatch service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudwatch/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cloudwatch.client import CloudWatchClient
from types_aiobotocore_cloudwatch.service_resource import CloudWatchServiceResource

from boto34.aioboto3.service_factory import ServiceResourceFactory


class CloudWatchService(ServiceResourceFactory[CloudWatchClient, CloudWatchServiceResource]):
    """
    CloudWatch service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudwatch/)
    """
