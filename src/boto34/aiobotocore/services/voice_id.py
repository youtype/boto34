"""
Wrapper for aiobotocore VoiceID service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/)

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
    # Returns type annotated aiobotocore VoiceID client
    async with session.voice_id.create_client() as voice_id_client:
        voice_id_client: types_aiobotocore_voice_id.client.VoiceIDClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_voice_id.client import VoiceIDClient
except ImportError:
    VoiceIDClient = object  # type: ignore[misc,assignment]


class VoiceIDService(
    ServiceFactory[VoiceIDClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "voice-id"
    _SERVICE_PROP = "voice_id"
