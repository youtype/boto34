"""
Wrapper for boto3 ChimeSDKMessaging service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_chime_sdk_messaging/)

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
    # Returns type annotated boto3 ChimeSDKMessaging client
    chime_sdk_messaging_client = session.chime_sdk_messaging.client()
    chime_sdk_messaging_client: types_boto3_chime_sdk_messaging.client.ChimeSDKMessagingClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_chime_sdk_messaging.client import ChimeSDKMessagingClient
except ImportError:
    ChimeSDKMessagingClient = object  # type: ignore[misc,assignment]


class ChimeSDKMessagingService(
    ServiceFactory[ChimeSDKMessagingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "chime-sdk-messaging"
    _SERVICE_PROP = "chime_sdk_messaging"
