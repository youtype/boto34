"""
Wrapper for boto3 SES service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ses/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_ses.client import SESClient

from boto34.boto3.service_factory import ServiceFactory


class SESService(ServiceFactory[SESClient]):
    """
    SES service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ses/)
    """
