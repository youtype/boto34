"""
Wrapper for aiobotocore PinpointSMSVoice service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_pinpoint_sms_voice.client import PinpointSMSVoiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class PinpointSMSVoiceService(ServiceFactory[PinpointSMSVoiceClient]):
    """
    PinpointSMSVoice service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice/)
    """
