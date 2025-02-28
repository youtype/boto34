"""
Wrapper for boto3 PinpointSMSVoice service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pinpoint_sms_voice/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_pinpoint_sms_voice.client import PinpointSMSVoiceClient

from boto34.boto3.service_factory import ServiceFactory


class PinpointSMSVoiceService(ServiceFactory[PinpointSMSVoiceClient]):
    """
    PinpointSMSVoice service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pinpoint_sms_voice/)
    """
