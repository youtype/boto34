"""
Wrapper for aiobotocore ChimeSDKMessaging service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_messaging/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_chime_sdk_messaging.client import ChimeSDKMessagingClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ChimeSDKMessagingService(ServiceFactory[ChimeSDKMessagingClient]):
    """
    ChimeSDKMessaging service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_messaging/)
    """
