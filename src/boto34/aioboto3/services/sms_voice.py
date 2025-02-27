"""
Wrapper for aioboto3 PinpointSMSVoice service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sms_voice/)

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
    # Returns type annotated aioboto3 PinpointSMSVoice client
    sms_voice_client = session.sms_voice.client()
    sms_voice_client: types_aiobotocore_sms_voice.client.PinpointSMSVoiceClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_sms_voice.client import PinpointSMSVoiceClient
except ImportError:
    PinpointSMSVoiceClient = object  # type: ignore[misc,assignment]


class PinpointSMSVoiceService(
    ServiceFactory[PinpointSMSVoiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sms-voice"
    _SERVICE_PROP = "sms_voice"
