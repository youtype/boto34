"""
Wrapper for aiobotocore SQS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sqs.client import SQSClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SQSService(ServiceFactory[SQSClient]):
    """
    SQS service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/)
    """
