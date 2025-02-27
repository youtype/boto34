"""
Wrapper for boto3 IoTDeviceAdvisor service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotdeviceadvisor/)

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
    # Returns type annotated boto3 IoTDeviceAdvisor client
    iotdeviceadvisor_client = session.iotdeviceadvisor.client()
    iotdeviceadvisor_client: types_boto3_iotdeviceadvisor.client.IoTDeviceAdvisorClient
    ```
"""

from __future__ import annotations

from types_boto3_iotdeviceadvisor.client import IoTDeviceAdvisorClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_iotdeviceadvisor.client import IoTDeviceAdvisorClient
except ImportError:
    IoTDeviceAdvisorClient = object  # type: ignore[misc,assignment]


class IoTDeviceAdvisorService(
    ServiceFactory[IoTDeviceAdvisorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iotdeviceadvisor"
    _SERVICE_PROP = "iotdeviceadvisor"
