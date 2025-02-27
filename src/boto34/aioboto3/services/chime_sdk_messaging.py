"""
Wrapper for aioboto3 ChimeSDKMessaging service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_chime_sdk_messaging/)

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
    # Returns type annotated aioboto3 ChimeSDKMessaging client
    chime_sdk_messaging_client = session.chime_sdk_messaging.client()
    chime_sdk_messaging_client: types_aiobotocore_chime_sdk_messaging.client.ChimeSDKMessagingClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_chime_sdk_messaging.client import ChimeSDKMessagingClient
except ImportError:
    ChimeSDKMessagingClient = object  # type: ignore[misc,assignment]


class ChimeSDKMessagingService(
    ServiceFactory[ChimeSDKMessagingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "chime-sdk-messaging"
    _SERVICE_PROP = "chime_sdk_messaging"
