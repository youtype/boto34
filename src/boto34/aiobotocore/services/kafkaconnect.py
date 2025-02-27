"""
Wrapper for aiobotocore KafkaConnect service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafkaconnect/)

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
    # Returns type annotated aiobotocore KafkaConnect client
    async with session.kafkaconnect.create_client() as kafkaconnect_client:
        kafkaconnect_client: types_aiobotocore_kafkaconnect.client.KafkaConnectClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_kafkaconnect.client import KafkaConnectClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_kafkaconnect.client import KafkaConnectClient
except ImportError:
    KafkaConnectClient = object  # type: ignore[misc,assignment]


class KafkaConnectService(
    ServiceFactory[KafkaConnectClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kafkaconnect"
    _SERVICE_PROP = "kafkaconnect"
