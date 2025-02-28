"""
Wrapper for boto3 EBS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ebs/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_ebs.client import EBSClient

from boto34.boto3.service_factory import ServiceFactory


class EBSService(ServiceFactory[EBSClient]):
    """
    EBS service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ebs/)
    """
