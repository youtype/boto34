"""
Wrapper for boto3 IoT service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iot/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_iot.client import IoTClient

from boto34.boto3.service_factory import ServiceFactory


class IoTService(ServiceFactory[IoTClient]):
    """
    IoT service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iot/)
    """
