"""
Wrapper for boto3 IoTWireless service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotwireless/)

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
    # Returns type annotated boto3 IoTWireless client
    iotwireless_client = session.iotwireless.client()
    iotwireless_client: types_boto3_iotwireless.client.IoTWirelessClient
    ```
"""

from __future__ import annotations

from types_boto3_iotwireless.client import IoTWirelessClient

from boto34.boto3.service_factory import ServiceFactory


class IoTWirelessService(ServiceFactory[IoTWirelessClient]):
    SERVICE_NAME = "iotwireless"
    _SERVICE_PROP = "iotwireless"
