"""
Wrapper for boto3 MailManager service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mailmanager/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_mailmanager.client import MailManagerClient

from boto34.boto3.service_factory import ServiceFactory


class MailManagerService(ServiceFactory[MailManagerClient]):
    """
    MailManager service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mailmanager/)
    """
