"""
Wrapper for boto3 EFS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_efs/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_efs.client import EFSClient

from boto34.boto3.service_factory import ServiceFactory


class EFSService(ServiceFactory[EFSClient]):
    """
    EFS service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_efs/)
    """
