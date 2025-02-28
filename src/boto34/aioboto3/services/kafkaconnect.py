"""
Wrapper for aioboto3 KafkaConnect service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kafkaconnect/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_kafkaconnect.client import KafkaConnectClient

from boto34.aioboto3.service_factory import ServiceFactory


class KafkaConnectService(ServiceFactory[KafkaConnectClient]):
    """
    KafkaConnect service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kafkaconnect/)
    """
