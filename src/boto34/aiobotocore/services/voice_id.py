"""
Wrapper for aiobotocore VoiceID service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_voice_id.client import VoiceIDClient

from boto34.aiobotocore.service_factory import ServiceFactory


class VoiceIDService(ServiceFactory[VoiceIDClient]):
    """
    VoiceID service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/)
    """
