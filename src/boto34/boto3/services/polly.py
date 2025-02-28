"""
Wrapper for boto3 Polly service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_polly/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_polly.client import PollyClient

from boto34.boto3.service_factory import ServiceFactory


class PollyService(ServiceFactory[PollyClient]):
    """
    Polly service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_polly/)
    """
