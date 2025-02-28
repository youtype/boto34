"""
Wrapper for boto3 RecycleBin service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_rbin/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_rbin.client import RecycleBinClient

from boto34.boto3.service_factory import ServiceFactory


class RecycleBinService(ServiceFactory[RecycleBinClient]):
    """
    RecycleBin service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_rbin/)
    """
