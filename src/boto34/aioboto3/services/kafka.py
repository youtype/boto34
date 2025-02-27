"""
Wrapper for aioboto3 Kafka service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kafka/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 Kafka client
    kafka_client = session.kafka.client()
    kafka_client: types_aiobotocore_kafka.client.KafkaClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_kafka.client import KafkaClient
except ImportError:
    KafkaClient = object  # type: ignore[misc,assignment]


class KafkaService(
    ServiceFactory[KafkaClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kafka"
    _SERVICE_PROP = "kafka"
