"""
Wrapper for aioboto3 PinpointSMSVoiceV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pinpoint_sms_voice_v2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_pinpoint_sms_voice_v2.client import PinpointSMSVoiceV2Client

from boto34.aioboto3.service_factory import ServiceFactory


class PinpointSMSVoiceV2Service(ServiceFactory[PinpointSMSVoiceV2Client]):
    """
    PinpointSMSVoiceV2 service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pinpoint_sms_voice_v2/)
    """
