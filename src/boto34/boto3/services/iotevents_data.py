"""
Wrapper for boto3 IoTEventsData service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotevents_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_iotevents_data.client import IoTEventsDataClient

from boto34.boto3.service_factory import ServiceFactory


class IoTEventsDataService(ServiceFactory[IoTEventsDataClient]):
    """
    IoTEventsData service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotevents_data/)
    """
