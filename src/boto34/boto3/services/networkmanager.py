"""
Wrapper for boto3 NetworkManager service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_networkmanager/)

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
    # Returns type annotated boto3 NetworkManager client
    networkmanager_client = session.networkmanager.client()
    networkmanager_client: types_boto3_networkmanager.client.NetworkManagerClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_networkmanager.client import NetworkManagerClient
except ImportError:
    NetworkManagerClient = object  # type: ignore[misc,assignment]


class NetworkManagerService(
    ServiceFactory[NetworkManagerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "networkmanager"
    _SERVICE_PROP = "networkmanager"
