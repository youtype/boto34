"""
Wrapper for aioboto3 SNS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sns/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sns.client import SNSClient
from types_aiobotocore_sns.service_resource import SNSServiceResource

from boto34.aioboto3.service_factory import ServiceResourceFactory


class SNSService(ServiceResourceFactory[SNSClient, SNSServiceResource]):
    """
    SNS service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sns/)
    """
