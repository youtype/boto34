"""
Wrapper for boto3 SMSVoice service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sms_voice/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_sms_voice.client import SMSVoiceClient

from boto34.boto3.service_factory import ServiceFactory


class SMSVoiceService(ServiceFactory[SMSVoiceClient]):
    """
    SMSVoice service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sms_voice/)
    """
