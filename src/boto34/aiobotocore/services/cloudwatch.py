"""
Wrapper for aiobotocore CloudWatch service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cloudwatch.client import CloudWatchClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudWatchService(ServiceFactory[CloudWatchClient]):
    """
    CloudWatch service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/)
    """
