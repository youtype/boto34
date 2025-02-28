"""
Wrapper for boto3 SNS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sns/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_sns.client import SNSClient
from types_boto3_sns.service_resource import SNSServiceResource

from boto34.boto3.service_factory import ServiceResourceFactory


class SNSService(ServiceResourceFactory[SNSClient, SNSServiceResource]):
    """
    SNS service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sns/)
    """
