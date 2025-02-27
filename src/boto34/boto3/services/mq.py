"""
Wrapper for boto3 MQ service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mq/)

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
    # Returns type annotated boto3 MQ client
    mq_client = session.mq.client()
    mq_client: types_boto3_mq.client.MQClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_mq.client import MQClient
except ImportError:
    MQClient = object  # type: ignore[misc,assignment]


class MQService(
    ServiceFactory[MQClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "mq"
    _SERVICE_PROP = "mq"
