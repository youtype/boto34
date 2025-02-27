"""
Wrapper for aioboto3 Kinesis service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kinesis/)

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
    # Returns type annotated aioboto3 Kinesis client
    kinesis_client = session.kinesis.client()
    kinesis_client: types_aiobotocore_kinesis.client.KinesisClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_kinesis.client import KinesisClient
except ImportError:
    KinesisClient = object  # type: ignore[misc,assignment]


class KinesisService(
    ServiceFactory[KinesisClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kinesis"
    _SERVICE_PROP = "kinesis"
