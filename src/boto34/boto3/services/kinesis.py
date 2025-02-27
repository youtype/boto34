"""
Wrapper for boto3 Kinesis service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis/)

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
    # Returns type annotated boto3 Kinesis client
    kinesis_client = session.kinesis.client()
    kinesis_client: types_boto3_kinesis.client.KinesisClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_kinesis.client import KinesisClient
except ImportError:
    KinesisClient = object  # type: ignore[misc,assignment]


class KinesisService(
    ServiceFactory[KinesisClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kinesis"
    _SERVICE_PROP = "kinesis"
