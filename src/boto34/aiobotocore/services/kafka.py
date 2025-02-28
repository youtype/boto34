"""
Wrapper for aiobotocore Kafka service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_kafka.client import KafkaClient

from boto34.aiobotocore.service_factory import ServiceFactory


class KafkaService(ServiceFactory[KafkaClient]):
    """
    Kafka service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/)
    """
