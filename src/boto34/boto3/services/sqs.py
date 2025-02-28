"""
Wrapper for boto3 SQS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sqs/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_sqs.client import SQSClient
from types_boto3_sqs.service_resource import SQSServiceResource

from boto34.boto3.service_factory import ServiceResourceFactory


class SQSService(ServiceResourceFactory[SQSClient, SQSServiceResource]):
    """
    SQS service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sqs/)
    """
