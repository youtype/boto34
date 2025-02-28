"""
Wrapper for aiobotocore IoTThingsGraph service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotthingsgraph/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_iotthingsgraph.client import IoTThingsGraphClient

from boto34.aiobotocore.service_factory import ServiceFactory


class IoTThingsGraphService(ServiceFactory[IoTThingsGraphClient]):
    """
    IoTThingsGraph service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotthingsgraph/)
    """
