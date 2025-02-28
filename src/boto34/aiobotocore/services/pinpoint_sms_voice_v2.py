"""
Wrapper for aiobotocore PinpointSMSVoiceV2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_pinpoint_sms_voice_v2.client import PinpointSMSVoiceV2Client

from boto34.aiobotocore.service_factory import ServiceFactory


class PinpointSMSVoiceV2Service(ServiceFactory[PinpointSMSVoiceV2Client]):
    """
    PinpointSMSVoiceV2 service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/)
    """
