"""
Wrapper for aioboto3 Ivsrealtime service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ivs_realtime/)

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
    # Returns type annotated aioboto3 Ivsrealtime client
    ivs_realtime_client = session.ivs_realtime.client()
    ivs_realtime_client: types_aiobotocore_ivs_realtime.client.IvsrealtimeClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_ivs_realtime.client import IvsrealtimeClient
except ImportError:
    IvsrealtimeClient = object  # type: ignore[misc,assignment]


class IvsrealtimeService(
    ServiceFactory[IvsrealtimeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ivs-realtime"
    _SERVICE_PROP = "ivs_realtime"
