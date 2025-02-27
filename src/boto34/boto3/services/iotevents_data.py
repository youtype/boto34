"""
Wrapper for boto3 IoTEventsData service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotevents_data/)

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
    # Returns type annotated boto3 IoTEventsData client
    iotevents_data_client = session.iotevents_data.client()
    iotevents_data_client: types_boto3_iotevents_data.client.IoTEventsDataClient
    ```
"""

from __future__ import annotations

from types_boto3_iotevents_data.client import IoTEventsDataClient

from boto34.boto3.service_factory import ServiceFactory


class IoTEventsDataService(ServiceFactory[IoTEventsDataClient]):
    SERVICE_NAME = "iotevents-data"
    _SERVICE_PROP = "iotevents_data"
