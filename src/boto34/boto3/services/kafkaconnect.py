"""
Wrapper for boto3 KafkaConnect service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kafkaconnect/)

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
    # Returns type annotated boto3 KafkaConnect client
    kafkaconnect_client = session.kafkaconnect.client()
    kafkaconnect_client: types_boto3_kafkaconnect.client.KafkaConnectClient
    ```
"""

from __future__ import annotations

from types_boto3_kafkaconnect.client import KafkaConnectClient

from boto34.boto3.service_factory import ServiceFactory


class KafkaConnectService(ServiceFactory[KafkaConnectClient]):
    SERVICE_NAME = "kafkaconnect"
    _SERVICE_PROP = "kafkaconnect"
