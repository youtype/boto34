"""
Wrapper for aiobotocore NetworkManager service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_networkmanager/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore NetworkManager client
    async with session.networkmanager.create_client() as networkmanager_client:
        networkmanager_client: types_aiobotocore_networkmanager.client.NetworkManagerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_networkmanager.client import NetworkManagerClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_networkmanager.client import NetworkManagerClient
except ImportError:
    NetworkManagerClient = object  # type: ignore[misc,assignment]


class NetworkManagerService(
    ServiceFactory[NetworkManagerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "networkmanager"
    _SERVICE_PROP = "networkmanager"
