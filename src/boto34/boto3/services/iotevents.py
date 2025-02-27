"""
Wrapper for boto3 IoTEvents service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotevents/)

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
    # Returns type annotated boto3 IoTEvents client
    iotevents_client = session.iotevents.client()
    iotevents_client: types_boto3_iotevents.client.IoTEventsClient
    ```
"""

from __future__ import annotations

from types_boto3_iotevents.client import IoTEventsClient

from boto34.boto3.service_factory import ServiceFactory


class IoTEventsService(ServiceFactory[IoTEventsClient]):
    SERVICE_NAME = "iotevents"
    _SERVICE_PROP = "iotevents"
