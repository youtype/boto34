"""
Wrapper for boto3 IoT service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iot/)

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
    # Returns type annotated boto3 IoT client
    iot_client = session.iot.client()
    iot_client: types_boto3_iot.client.IoTClient
    ```
"""

from __future__ import annotations

from types_boto3_iot.client import IoTClient

from boto34.boto3.service_factory import ServiceFactory


class IoTService(ServiceFactory[IoTClient]):
    SERVICE_NAME = "iot"
    _SERVICE_PROP = "iot"
