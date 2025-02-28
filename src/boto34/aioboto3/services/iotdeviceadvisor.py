"""
Wrapper for aioboto3 IoTDeviceAdvisor service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iotdeviceadvisor/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_iotdeviceadvisor.client import IoTDeviceAdvisorClient

from boto34.aioboto3.service_factory import ServiceFactory


class IoTDeviceAdvisorService(ServiceFactory[IoTDeviceAdvisorClient]):
    """
    IoTDeviceAdvisor service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iotdeviceadvisor/)
    """
