"""
Wrapper for aiobotocore SMSVoice service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sms_voice/)

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
    # Returns type annotated aiobotocore SMSVoice client
    async with session.sms_voice.create_client() as sms_voice_client:
        sms_voice_client: types_aiobotocore_sms_voice.client.SMSVoiceClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_sms_voice.client import SMSVoiceClient
except ImportError:
    SMSVoiceClient = object  # type: ignore[misc,assignment]


class SMSVoiceService(
    ServiceFactory[SMSVoiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sms-voice"
    _SERVICE_PROP = "sms_voice"
