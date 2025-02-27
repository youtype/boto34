"""
Wrapper for aiobotocore Connect service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/)

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
    # Returns type annotated aiobotocore Connect client
    async with session.connect.create_client() as connect_client:
        connect_client: types_aiobotocore_connect.client.ConnectClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_connect.client import ConnectClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_connect.client import ConnectClient
except ImportError:
    ConnectClient = object  # type: ignore[misc,assignment]


class ConnectService(
    ServiceFactory[ConnectClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "connect"
    _SERVICE_PROP = "connect"
