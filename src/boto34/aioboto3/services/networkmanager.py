"""
Wrapper for aioboto3 NetworkManager service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_networkmanager/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 NetworkManager client
    networkmanager_client = session.networkmanager.client()
    networkmanager_client: types_aiobotocore_networkmanager.client.NetworkManagerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_networkmanager.client import NetworkManagerClient

from boto34.aioboto3.service_factory import ServiceFactory


class NetworkManagerService(ServiceFactory[NetworkManagerClient]):
    SERVICE_NAME = "networkmanager"
    _SERVICE_PROP = "networkmanager"
