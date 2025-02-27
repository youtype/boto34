"""
Wrapper for boto3 ChimeSDKVoice service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_chime_sdk_voice/)

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
    # Returns type annotated boto3 ChimeSDKVoice client
    chime_sdk_voice_client = session.chime_sdk_voice.client()
    chime_sdk_voice_client: types_boto3_chime_sdk_voice.client.ChimeSDKVoiceClient
    ```
"""

from __future__ import annotations

from types_boto3_chime_sdk_voice.client import ChimeSDKVoiceClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_chime_sdk_voice.client import ChimeSDKVoiceClient
except ImportError:
    ChimeSDKVoiceClient = object  # type: ignore[misc,assignment]


class ChimeSDKVoiceService(
    ServiceFactory[ChimeSDKVoiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "chime-sdk-voice"
    _SERVICE_PROP = "chime_sdk_voice"
