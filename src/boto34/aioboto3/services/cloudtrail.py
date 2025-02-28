"""
Wrapper for aioboto3 CloudTrail service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudtrail/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cloudtrail.client import CloudTrailClient

from boto34.aioboto3.service_factory import ServiceFactory


class CloudTrailService(ServiceFactory[CloudTrailClient]):
    """
    CloudTrail service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudtrail/)
    """
