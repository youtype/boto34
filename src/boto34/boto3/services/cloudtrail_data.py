"""
Wrapper for boto3 CloudTrailDataService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudtrail_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_cloudtrail_data.client import CloudTrailDataServiceClient

from boto34.boto3.service_factory import ServiceFactory


class CloudTrailDataServiceService(ServiceFactory[CloudTrailDataServiceClient]):
    """
    CloudTrailDataService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudtrail_data/)
    """
