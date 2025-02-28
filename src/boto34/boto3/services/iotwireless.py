"""
Wrapper for boto3 IoTWireless service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotwireless/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_iotwireless.client import IoTWirelessClient

from boto34.boto3.service_factory import ServiceFactory


class IoTWirelessService(ServiceFactory[IoTWirelessClient]):
    """
    IoTWireless service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotwireless/)
    """
