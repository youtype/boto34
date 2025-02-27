"""
Wrapper for aiobotocore Kinesis service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesis/)

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
    # Returns type annotated aiobotocore Kinesis client
    async with session.kinesis.create_client() as kinesis_client:
        kinesis_client: types_aiobotocore_kinesis.client.KinesisClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_kinesis.client import KinesisClient
except ImportError:
    KinesisClient = object  # type: ignore[misc,assignment]


class KinesisService(
    ServiceFactory[KinesisClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kinesis"
    _SERVICE_PROP = "kinesis"
