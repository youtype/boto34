"""
Wrapper for aiobotocore Ivsrealtime service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/)

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
    # Returns type annotated aiobotocore Ivsrealtime client
    async with session.ivs_realtime.create_client() as ivs_realtime_client:
        ivs_realtime_client: types_aiobotocore_ivs_realtime.client.IvsrealtimeClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_ivs_realtime.client import IvsrealtimeClient
except ImportError:
    IvsrealtimeClient = object  # type: ignore[misc,assignment]


class IvsrealtimeService(
    ServiceFactory[IvsrealtimeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ivs-realtime"
    _SERVICE_PROP = "ivs_realtime"
