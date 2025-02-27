"""
Wrapper for boto3 PinpointSMSVoiceV2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pinpoint_sms_voice_v2/)

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
    # Returns type annotated boto3 PinpointSMSVoiceV2 client
    pinpoint_sms_voice_v2_client = session.pinpoint_sms_voice_v2.client()
    pinpoint_sms_voice_v2_client: types_boto3_pinpoint_sms_voice_v2.client.PinpointSMSVoiceV2Client
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_pinpoint_sms_voice_v2.client import PinpointSMSVoiceV2Client
except ImportError:
    PinpointSMSVoiceV2Client = object  # type: ignore[misc,assignment]


class PinpointSMSVoiceV2Service(
    ServiceFactory[PinpointSMSVoiceV2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "pinpoint-sms-voice-v2"
    _SERVICE_PROP = "pinpoint_sms_voice_v2"
