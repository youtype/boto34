"""
Wrapper for aioboto3 CloudTrailDataService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudtrail_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cloudtrail_data.client import CloudTrailDataServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class CloudTrailDataServiceService(ServiceFactory[CloudTrailDataServiceClient]):
    """
    CloudTrailDataService service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudtrail_data/)
    """
