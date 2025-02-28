"""
Wrapper for boto3 FIS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_fis/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_fis.client import FISClient

from boto34.boto3.service_factory import ServiceFactory


class FISService(ServiceFactory[FISClient]):
    """
    FIS service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_fis/)
    """
