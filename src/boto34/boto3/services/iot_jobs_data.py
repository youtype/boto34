"""
Wrapper for boto3 IoTJobsDataPlane service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iot_jobs_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_iot_jobs_data.client import IoTJobsDataPlaneClient

from boto34.boto3.service_factory import ServiceFactory


class IoTJobsDataPlaneService(ServiceFactory[IoTJobsDataPlaneClient]):
    """
    IoTJobsDataPlane service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iot_jobs_data/)
    """
