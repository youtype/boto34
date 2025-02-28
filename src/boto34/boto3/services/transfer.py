"""
Wrapper for boto3 Transfer service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_transfer/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_transfer.client import TransferClient

from boto34.boto3.service_factory import ServiceFactory


class TransferService(ServiceFactory[TransferClient]):
    """
    Transfer service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_transfer/)
    """
