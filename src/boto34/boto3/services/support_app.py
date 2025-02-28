"""
Wrapper for boto3 SupportApp service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_support_app/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_support_app.client import SupportAppClient

from boto34.boto3.service_factory import ServiceFactory


class SupportAppService(ServiceFactory[SupportAppClient]):
    """
    SupportApp service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_support_app/)
    """
