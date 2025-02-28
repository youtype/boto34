"""
Wrapper for aiobotocore IoTJobsDataPlane service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iot_jobs_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_iot_jobs_data.client import IoTJobsDataPlaneClient

from boto34.aiobotocore.service_factory import ServiceFactory


class IoTJobsDataPlaneService(ServiceFactory[IoTJobsDataPlaneClient]):
    """
    IoTJobsDataPlane service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iot_jobs_data/)
    """
