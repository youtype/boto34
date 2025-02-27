"""
Wrapper for boto3 IoTJobsDataPlane service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iot_jobs_data/)

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
    # Returns type annotated boto3 IoTJobsDataPlane client
    iot_jobs_data_client = session.iot_jobs_data.client()
    iot_jobs_data_client: types_boto3_iot_jobs_data.client.IoTJobsDataPlaneClient
    ```
"""

from __future__ import annotations

from types_boto3_iot_jobs_data.client import IoTJobsDataPlaneClient

from boto34.boto3.service_factory import ServiceFactory


class IoTJobsDataPlaneService(ServiceFactory[IoTJobsDataPlaneClient]):
    SERVICE_NAME = "iot-jobs-data"
    _SERVICE_PROP = "iot_jobs_data"
