"""
Wrapper for aioboto3 IoTFleetHub service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iotfleethub/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_iotfleethub.client import IoTFleetHubClient

from boto34.aioboto3.service_factory import ServiceFactory


class IoTFleetHubService(ServiceFactory[IoTFleetHubClient]):
    """
    IoTFleetHub service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iotfleethub/)
    """
