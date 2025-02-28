"""
Wrapper for boto3 SMS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sms/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_sms.client import SMSClient

from boto34.boto3.service_factory import ServiceFactory


class SMSService(ServiceFactory[SMSClient]):
    """
    SMS service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sms/)
    """
