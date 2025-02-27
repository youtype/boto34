"""
Wrapper for aioboto3 ChimeSDKVoice service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_chime_sdk_voice/)

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
    # Returns type annotated aioboto3 ChimeSDKVoice client
    chime_sdk_voice_client = session.chime_sdk_voice.client()
    chime_sdk_voice_client: types_aiobotocore_chime_sdk_voice.client.ChimeSDKVoiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_chime_sdk_voice.client import ChimeSDKVoiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class ChimeSDKVoiceService(ServiceFactory[ChimeSDKVoiceClient]):
    SERVICE_NAME = "chime-sdk-voice"
    _SERVICE_PROP = "chime_sdk_voice"
