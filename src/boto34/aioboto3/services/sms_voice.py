"""
Wrapper for aioboto3 SMSVoice service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sms_voice/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sms_voice.client import SMSVoiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class SMSVoiceService(ServiceFactory[SMSVoiceClient]):
    """
    SMSVoice service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sms_voice/)
    """
