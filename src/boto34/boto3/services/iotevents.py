"""
Wrapper for boto3 IoTEvents service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotevents/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_iotevents.client import IoTEventsClient

from boto34.boto3.service_factory import ServiceFactory


class IoTEventsService(ServiceFactory[IoTEventsClient]):
    """
    IoTEvents service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotevents/)
    """
