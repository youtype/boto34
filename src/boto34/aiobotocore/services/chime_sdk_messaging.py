"""
Wrapper for aiobotocore ChimeSDKMessaging service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_messaging/)

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
    # Returns type annotated aiobotocore ChimeSDKMessaging client
    async with session.chime_sdk_messaging.create_client() as chime_sdk_messaging_client:
        chime_sdk_messaging_client: types_aiobotocore_chime_sdk_messaging.client.ChimeSDKMessagingClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_chime_sdk_messaging.client import ChimeSDKMessagingClient
except ImportError:
    ChimeSDKMessagingClient = object  # type: ignore[misc,assignment]


class ChimeSDKMessagingService(
    ServiceFactory[ChimeSDKMessagingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "chime-sdk-messaging"
    _SERVICE_PROP = "chime_sdk_messaging"
