"""
Wrapper for aiobotocore SMS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sms/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sms.client import SMSClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SMSService(ServiceFactory[SMSClient]):
    """
    SMS service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sms/)
    """
