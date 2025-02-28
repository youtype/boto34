"""
Wrapper for aioboto3 VoiceID service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_voice_id/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_voice_id.client import VoiceIDClient

from boto34.aioboto3.service_factory import ServiceFactory


class VoiceIDService(ServiceFactory[VoiceIDClient]):
    """
    VoiceID service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_voice_id/)
    """
