"""
Wrapper for aiobotocore PinpointSMSVoiceV2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/)

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
    # Returns type annotated aiobotocore PinpointSMSVoiceV2 client
    async with session.pinpoint_sms_voice_v2.create_client() as pinpoint_sms_voice_v2_client:
        pinpoint_sms_voice_v2_client: (
            types_aiobotocore_pinpoint_sms_voice_v2.client.PinpointSMSVoiceV2Client
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_pinpoint_sms_voice_v2.client import PinpointSMSVoiceV2Client

from boto34.aiobotocore.service_factory import ServiceFactory


class PinpointSMSVoiceV2Service(ServiceFactory[PinpointSMSVoiceV2Client]):
    SERVICE_NAME = "pinpoint-sms-voice-v2"
    _SERVICE_PROP = "pinpoint_sms_voice_v2"
