"""
Wrapper for boto3 KafkaConnect service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kafkaconnect/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_kafkaconnect.client import KafkaConnectClient

from boto34.boto3.service_factory import ServiceFactory


class KafkaConnectService(ServiceFactory[KafkaConnectClient]):
    """
    KafkaConnect service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kafkaconnect/)
    """
