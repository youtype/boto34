"""
Wrapper for boto3 IoTDeviceAdvisor service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotdeviceadvisor/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_iotdeviceadvisor.client import IoTDeviceAdvisorClient

from boto34.boto3.service_factory import ServiceFactory


class IoTDeviceAdvisorService(ServiceFactory[IoTDeviceAdvisorClient]):
    """
    IoTDeviceAdvisor service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotdeviceadvisor/)
    """
