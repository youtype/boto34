"""
Wrapper for boto3 ACM service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_acm/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_acm.client import ACMClient

from boto34.boto3.service_factory import ServiceFactory


class ACMService(ServiceFactory[ACMClient]):
    """
    ACM service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_acm/)
    """
