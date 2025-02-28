"""
Wrapper for aiobotocore IoTFleetWise service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_iotfleetwise.client import IoTFleetWiseClient

from boto34.aiobotocore.service_factory import ServiceFactory


class IoTFleetWiseService(ServiceFactory[IoTFleetWiseClient]):
    """
    IoTFleetWise service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/)
    """
