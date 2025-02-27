"""
Wrapper for aiobotocore Kafka service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore Kafka client
    async with session.kafka.create_client() as kafka_client:
        kafka_client: types_aiobotocore_kafka.client.KafkaClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_kafka.client import KafkaClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_kafka.client import KafkaClient
except ImportError:
    KafkaClient = object  # type: ignore[misc,assignment]


class KafkaService(
    ServiceFactory[KafkaClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kafka"
    _SERVICE_PROP = "kafka"
