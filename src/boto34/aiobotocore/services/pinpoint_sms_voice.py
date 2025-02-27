"""
Wrapper for aiobotocore PinpointSMSVoice service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice/)

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
    # Returns type annotated aiobotocore PinpointSMSVoice client
    async with session.pinpoint_sms_voice.create_client() as pinpoint_sms_voice_client:
        pinpoint_sms_voice_client: types_aiobotocore_pinpoint_sms_voice.client.PinpointSMSVoiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_pinpoint_sms_voice.client import PinpointSMSVoiceClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_pinpoint_sms_voice.client import PinpointSMSVoiceClient
except ImportError:
    PinpointSMSVoiceClient = object  # type: ignore[misc,assignment]


class PinpointSMSVoiceService(
    ServiceFactory[PinpointSMSVoiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "pinpoint-sms-voice"
    _SERVICE_PROP = "pinpoint_sms_voice"
