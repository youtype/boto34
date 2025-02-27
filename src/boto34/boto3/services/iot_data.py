"""
Wrapper for boto3 IoTDataPlane service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iot_data/)

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
    # Returns type annotated boto3 IoTDataPlane client
    iot_data_client = session.iot_data.client()
    iot_data_client: types_boto3_iot_data.client.IoTDataPlaneClient
    ```
"""

from __future__ import annotations

from types_boto3_iot_data.client import IoTDataPlaneClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_iot_data.client import IoTDataPlaneClient
except ImportError:
    IoTDataPlaneClient = object  # type: ignore[misc,assignment]


class IoTDataPlaneService(
    ServiceFactory[IoTDataPlaneClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iot-data"
    _SERVICE_PROP = "iot_data"
