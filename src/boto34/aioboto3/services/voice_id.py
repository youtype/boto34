"""
Wrapper for aioboto3 VoiceID service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_voice_id/)

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
    # Returns type annotated aioboto3 VoiceID client
    voice_id_client = session.voice_id.client()
    voice_id_client: types_aiobotocore_voice_id.client.VoiceIDClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_voice_id.client import VoiceIDClient

from boto34.aioboto3.service_factory import ServiceFactory


class VoiceIDService(ServiceFactory[VoiceIDClient]):
    SERVICE_NAME = "voice-id"
    _SERVICE_PROP = "voice_id"
