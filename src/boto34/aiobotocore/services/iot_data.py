"""
Wrapper for aiobotocore IoTDataPlane service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iot_data/)

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
    # Returns type annotated aiobotocore IoTDataPlane client
    async with session.iot_data.create_client() as iot_data_client:
        iot_data_client: types_aiobotocore_iot_data.client.IoTDataPlaneClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_iot_data.client import IoTDataPlaneClient

from boto34.aiobotocore.service_factory import ServiceFactory


class IoTDataPlaneService(ServiceFactory[IoTDataPlaneClient]):
    SERVICE_NAME = "iot-data"
    _SERVICE_PROP = "iot_data"
