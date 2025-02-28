"""
Wrapper for aioboto3 ChimeSDKVoice service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_chime_sdk_voice/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_chime_sdk_voice.client import ChimeSDKVoiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class ChimeSDKVoiceService(ServiceFactory[ChimeSDKVoiceClient]):
    """
    ChimeSDKVoice service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_chime_sdk_voice/)
    """
