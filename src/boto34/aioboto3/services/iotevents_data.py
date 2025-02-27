"""
Wrapper for aioboto3 IoTEventsData service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iotevents_data/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 IoTEventsData client
    iotevents_data_client = session.iotevents_data.client()
    iotevents_data_client: types_aiobotocore_iotevents_data.client.IoTEventsDataClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_iotevents_data.client import IoTEventsDataClient

from boto34.aioboto3.service_factory import ServiceFactory


class IoTEventsDataService(ServiceFactory[IoTEventsDataClient]):
    SERVICE_NAME = "iotevents-data"
    _SERVICE_PROP = "iotevents_data"
