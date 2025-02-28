"""
Wrapper for aioboto3 IoTJobsDataPlane service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iot_jobs_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_iot_jobs_data.client import IoTJobsDataPlaneClient

from boto34.aioboto3.service_factory import ServiceFactory


class IoTJobsDataPlaneService(ServiceFactory[IoTJobsDataPlaneClient]):
    """
    IoTJobsDataPlane service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iot_jobs_data/)
    """
