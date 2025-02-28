"""
Wrapper for aiobotocore IoTEvents service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotevents/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_iotevents.client import IoTEventsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class IoTEventsService(ServiceFactory[IoTEventsClient]):
    """
    IoTEvents service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotevents/)
    """
