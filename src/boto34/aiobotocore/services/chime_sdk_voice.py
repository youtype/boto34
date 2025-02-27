"""
Wrapper for aiobotocore ChimeSDKVoice service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_voice/)

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
    # Returns type annotated aiobotocore ChimeSDKVoice client
    async with session.chime_sdk_voice.create_client() as chime_sdk_voice_client:
        chime_sdk_voice_client: types_aiobotocore_chime_sdk_voice.client.ChimeSDKVoiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_chime_sdk_voice.client import ChimeSDKVoiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ChimeSDKVoiceService(ServiceFactory[ChimeSDKVoiceClient]):
    SERVICE_NAME = "chime-sdk-voice"
    _SERVICE_PROP = "chime_sdk_voice"
