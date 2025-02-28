"""
Wrapper for boto3 MQ service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mq/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_mq.client import MQClient

from boto34.boto3.service_factory import ServiceFactory


class MQService(ServiceFactory[MQClient]):
    """
    MQ service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mq/)
    """
