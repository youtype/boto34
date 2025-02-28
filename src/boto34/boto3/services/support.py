"""
Wrapper for boto3 Support service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_support/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_support.client import SupportClient

from boto34.boto3.service_factory import ServiceFactory


class SupportService(ServiceFactory[SupportClient]):
    """
    Support service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_support/)
    """
