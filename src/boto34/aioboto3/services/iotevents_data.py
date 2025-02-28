"""
Wrapper for aioboto3 IoTEventsData service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iotevents_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_iotevents_data.client import IoTEventsDataClient

from boto34.aioboto3.service_factory import ServiceFactory


class IoTEventsDataService(ServiceFactory[IoTEventsDataClient]):
    """
    IoTEventsData service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iotevents_data/)
    """
