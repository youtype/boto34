"""
Wrapper for boto3 IAM service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iam/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_iam.client import IAMClient
from types_boto3_iam.service_resource import IAMServiceResource

from boto34.boto3.service_factory import ServiceResourceFactory


class IAMService(ServiceResourceFactory[IAMClient, IAMServiceResource]):
    """
    IAM service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iam/)
    """
