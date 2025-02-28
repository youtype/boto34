"""
Wrapper for aiobotocore NetworkManager service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_networkmanager/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_networkmanager.client import NetworkManagerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class NetworkManagerService(ServiceFactory[NetworkManagerClient]):
    """
    NetworkManager service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_networkmanager/)
    """
