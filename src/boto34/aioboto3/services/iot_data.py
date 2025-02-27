"""
Wrapper for aioboto3 IoTDataPlane service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iot_data/)

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
    # Returns type annotated aioboto3 IoTDataPlane client
    iot_data_client = session.iot_data.client()
    iot_data_client: types_aiobotocore_iot_data.client.IoTDataPlaneClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_iot_data.client import IoTDataPlaneClient
except ImportError:
    IoTDataPlaneClient = object  # type: ignore[misc,assignment]


class IoTDataPlaneService(
    ServiceFactory[IoTDataPlaneClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iot-data"
    _SERVICE_PROP = "iot_data"
