"""
Wrapper for aioboto3 Connect service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_connect/)

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
    # Returns type annotated aioboto3 Connect client
    connect_client = session.connect.client()
    connect_client: types_aiobotocore_connect.client.ConnectClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_connect.client import ConnectClient
except ImportError:
    ConnectClient = object  # type: ignore[misc,assignment]


class ConnectService(
    ServiceFactory[ConnectClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "connect"
    _SERVICE_PROP = "connect"
