"""
Wrapper for aioboto3 PinpointSMSVoiceV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pinpoint_sms_voice_v2/)

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
    # Returns type annotated aioboto3 PinpointSMSVoiceV2 client
    pinpoint_sms_voice_v2_client = session.pinpoint_sms_voice_v2.client()
    pinpoint_sms_voice_v2_client: (
        types_aiobotocore_pinpoint_sms_voice_v2.client.PinpointSMSVoiceV2Client
    )
    ```
"""

from __future__ import annotations

from types_aiobotocore_pinpoint_sms_voice_v2.client import PinpointSMSVoiceV2Client

from boto34.aioboto3.service_factory import ServiceFactory


class PinpointSMSVoiceV2Service(ServiceFactory[PinpointSMSVoiceV2Client]):
    SERVICE_NAME = "pinpoint-sms-voice-v2"
    _SERVICE_PROP = "pinpoint_sms_voice_v2"
