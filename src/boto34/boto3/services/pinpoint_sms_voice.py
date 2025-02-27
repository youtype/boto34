"""
Wrapper for boto3 PinpointSMSVoice service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pinpoint_sms_voice/)

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
    # Returns type annotated boto3 PinpointSMSVoice client
    pinpoint_sms_voice_client = session.pinpoint_sms_voice.client()
    pinpoint_sms_voice_client: types_boto3_pinpoint_sms_voice.client.PinpointSMSVoiceClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_pinpoint_sms_voice.client import PinpointSMSVoiceClient
except ImportError:
    PinpointSMSVoiceClient = object  # type: ignore[misc,assignment]


class PinpointSMSVoiceService(
    ServiceFactory[PinpointSMSVoiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "pinpoint-sms-voice"
    _SERVICE_PROP = "pinpoint_sms_voice"
