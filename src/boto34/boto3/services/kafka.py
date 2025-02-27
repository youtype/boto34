"""
Wrapper for boto3 Kafka service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kafka/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 Kafka client
    kafka_client = session.kafka.client()
    kafka_client: types_boto3_kafka.client.KafkaClient
    ```
"""

from __future__ import annotations

from types_boto3_kafka.client import KafkaClient

from boto34.boto3.service_factory import ServiceFactory


class KafkaService(ServiceFactory[KafkaClient]):
    SERVICE_NAME = "kafka"
    _SERVICE_PROP = "kafka"
