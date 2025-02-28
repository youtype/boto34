"""
Wrapper for boto3 ChimeSDKMessaging service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_chime_sdk_messaging/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_chime_sdk_messaging.client import ChimeSDKMessagingClient

from boto34.boto3.service_factory import ServiceFactory


class ChimeSDKMessagingService(ServiceFactory[ChimeSDKMessagingClient]):
    """
    ChimeSDKMessaging service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_chime_sdk_messaging/)
    """
