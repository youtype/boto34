"""
Wrapper for boto3 SMSVoice service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sms_voice/)

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
    # Returns type annotated boto3 SMSVoice client
    sms_voice_client = session.sms_voice.client()
    sms_voice_client: types_boto3_sms_voice.client.SMSVoiceClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_sms_voice.client import SMSVoiceClient
except ImportError:
    SMSVoiceClient = object  # type: ignore[misc,assignment]


class SMSVoiceService(
    ServiceFactory[SMSVoiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sms-voice"
    _SERVICE_PROP = "sms_voice"
