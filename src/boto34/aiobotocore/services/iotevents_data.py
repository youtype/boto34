"""
Wrapper for aiobotocore IoTEventsData service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotevents_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_iotevents_data.client import IoTEventsDataClient

from boto34.aiobotocore.service_factory import ServiceFactory


class IoTEventsDataService(ServiceFactory[IoTEventsDataClient]):
    """
    IoTEventsData service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotevents_data/)
    """
