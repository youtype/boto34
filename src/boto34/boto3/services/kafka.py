"""
Wrapper for boto3 Kafka service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kafka/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_kafka.client import KafkaClient

from boto34.boto3.service_factory import ServiceFactory


class KafkaService(ServiceFactory[KafkaClient]):
    """
    Kafka service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kafka/)
    """
