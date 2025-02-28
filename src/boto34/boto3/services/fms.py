"""
Wrapper for boto3 FMS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_fms/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_fms.client import FMSClient

from boto34.boto3.service_factory import ServiceFactory


class FMSService(ServiceFactory[FMSClient]):
    """
    FMS service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_fms/)
    """
