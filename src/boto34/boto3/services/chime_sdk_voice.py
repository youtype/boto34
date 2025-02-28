"""
Wrapper for boto3 ChimeSDKVoice service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_chime_sdk_voice/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_chime_sdk_voice.client import ChimeSDKVoiceClient

from boto34.boto3.service_factory import ServiceFactory


class ChimeSDKVoiceService(ServiceFactory[ChimeSDKVoiceClient]):
    """
    ChimeSDKVoice service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_chime_sdk_voice/)
    """
