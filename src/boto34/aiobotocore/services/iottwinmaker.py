"""
Wrapper for aiobotocore IoTTwinMaker service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_iottwinmaker.client import IoTTwinMakerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class IoTTwinMakerService(ServiceFactory[IoTTwinMakerClient]):
    """
    IoTTwinMaker service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/)
    """
