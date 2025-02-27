"""
Wrapper for boto3 VoiceID service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_voice_id/)

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
    # Returns type annotated boto3 VoiceID client
    voice_id_client = session.voice_id.client()
    voice_id_client: types_boto3_voice_id.client.VoiceIDClient
    ```
"""

from __future__ import annotations

from types_boto3_voice_id.client import VoiceIDClient

from boto34.boto3.service_factory import ServiceFactory


class VoiceIDService(ServiceFactory[VoiceIDClient]):
    SERVICE_NAME = "voice-id"
    _SERVICE_PROP = "voice_id"
