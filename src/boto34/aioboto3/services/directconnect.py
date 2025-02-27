"""
Wrapper for aioboto3 DirectConnect service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_directconnect/)

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
    # Returns type annotated aioboto3 DirectConnect client
    directconnect_client = session.directconnect.client()
    directconnect_client: types_aiobotocore_directconnect.client.DirectConnectClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_directconnect.client import DirectConnectClient
except ImportError:
    DirectConnectClient = object  # type: ignore[misc,assignment]


class DirectConnectService(
    ServiceFactory[DirectConnectClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "directconnect"
    _SERVICE_PROP = "directconnect"
