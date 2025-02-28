"""
Wrapper for boto3 STS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sts/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_sts.client import STSClient

from boto34.boto3.service_factory import ServiceFactory


class STSService(ServiceFactory[STSClient]):
    """
    STS service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sts/)
    """
