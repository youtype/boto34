"""
Wrapper for aioboto3 SQS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sqs/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sqs.client import SQSClient
from types_aiobotocore_sqs.service_resource import SQSServiceResource

from boto34.aioboto3.service_factory import ServiceResourceFactory


class SQSService(ServiceResourceFactory[SQSClient, SQSServiceResource]):
    """
    SQS service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sqs/)
    """
