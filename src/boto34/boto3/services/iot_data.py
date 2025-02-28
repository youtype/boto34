"""
Wrapper for boto3 IoTDataPlane service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iot_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_iot_data.client import IoTDataPlaneClient

from boto34.boto3.service_factory import ServiceFactory


class IoTDataPlaneService(ServiceFactory[IoTDataPlaneClient]):
    """
    IoTDataPlane service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iot_data/)
    """
