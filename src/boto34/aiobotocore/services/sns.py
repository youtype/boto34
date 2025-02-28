"""
Wrapper for aiobotocore SNS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sns/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sns.client import SNSClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SNSService(ServiceFactory[SNSClient]):
    """
    SNS service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sns/)
    """
