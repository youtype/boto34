"""
Wrapper for aiobotocore IoTJobsDataPlane service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iot_jobs_data/)

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
    # Returns type annotated aiobotocore IoTJobsDataPlane client
    async with session.iot_jobs_data.create_client() as iot_jobs_data_client:
        iot_jobs_data_client: types_aiobotocore_iot_jobs_data.client.IoTJobsDataPlaneClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_iot_jobs_data.client import IoTJobsDataPlaneClient
except ImportError:
    IoTJobsDataPlaneClient = object  # type: ignore[misc,assignment]


class IoTJobsDataPlaneService(
    ServiceFactory[IoTJobsDataPlaneClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iot-jobs-data"
    _SERVICE_PROP = "iot_jobs_data"
