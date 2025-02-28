"""
Wrapper for aiobotocore IoTDeviceAdvisor service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotdeviceadvisor/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_iotdeviceadvisor.client import IoTDeviceAdvisorClient

from boto34.aiobotocore.service_factory import ServiceFactory


class IoTDeviceAdvisorService(ServiceFactory[IoTDeviceAdvisorClient]):
    """
    IoTDeviceAdvisor service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotdeviceadvisor/)
    """
