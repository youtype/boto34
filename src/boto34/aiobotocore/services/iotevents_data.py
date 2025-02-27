"""
Wrapper for aiobotocore IoTEventsData service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotevents_data/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore IoTEventsData client
    async with session.iotevents_data.create_client() as iotevents_data_client:
        iotevents_data_client: types_aiobotocore_iotevents_data.client.IoTEventsDataClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_iotevents_data.client import IoTEventsDataClient

from boto34.aiobotocore.service_factory import ServiceFactory


class IoTEventsDataService(ServiceFactory[IoTEventsDataClient]):
    SERVICE_NAME = "iotevents-data"
    _SERVICE_PROP = "iotevents_data"
