"""
Wrapper for aiobotocore IoTSecureTunneling service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsecuretunneling/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_iotsecuretunneling.client import IoTSecureTunnelingClient

from boto34.aiobotocore.service_factory import ServiceFactory


class IoTSecureTunnelingService(ServiceFactory[IoTSecureTunnelingClient]):
    """
    IoTSecureTunneling service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsecuretunneling/)
    """
