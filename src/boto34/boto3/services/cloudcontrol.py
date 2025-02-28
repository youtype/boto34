"""
Wrapper for boto3 CloudControlApi service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudcontrol/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_cloudcontrol.client import CloudControlApiClient

from boto34.boto3.service_factory import ServiceFactory


class CloudControlApiService(ServiceFactory[CloudControlApiClient]):
    """
    CloudControlApi service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudcontrol/)
    """
