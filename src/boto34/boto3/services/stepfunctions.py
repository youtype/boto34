"""
Wrapper for boto3 SFN service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_stepfunctions/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_stepfunctions.client import SFNClient

from boto34.boto3.service_factory import ServiceFactory


class SFNService(ServiceFactory[SFNClient]):
    """
    SFN service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_stepfunctions/)
    """
