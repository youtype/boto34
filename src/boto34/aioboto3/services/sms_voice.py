"""
Wrapper for aioboto3 SMSVoice service.

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
    # Returns type annotated aioboto3 SMSVoice client
    sms_voice_client = session.sms_voice.client()
    sms_voice_client: types_aiobotocore_sms_voice.client.SMSVoiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_sms_voice.client import SMSVoiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class SMSVoiceService(ServiceFactory[SMSVoiceClient]):
    SERVICE_NAME = "sms-voice"
    _SERVICE_PROP = "sms_voice"
