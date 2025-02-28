"""
Wrapper for boto3 Comprehend service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_comprehend/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_comprehend.client import ComprehendClient

from boto34.boto3.service_factory import ServiceFactory


class ComprehendService(ServiceFactory[ComprehendClient]):
    """
    Comprehend service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_comprehend/)
    """
