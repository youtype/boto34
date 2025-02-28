"""
Wrapper for aioboto3 IoTDataPlane service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iot_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_iot_data.client import IoTDataPlaneClient

from boto34.aioboto3.service_factory import ServiceFactory


class IoTDataPlaneService(ServiceFactory[IoTDataPlaneClient]):
    """
    IoTDataPlane service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iot_data/)
    """
