"""
Wrapper for boto3 RAM service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ram/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_ram.client import RAMClient

from boto34.boto3.service_factory import ServiceFactory


class RAMService(ServiceFactory[RAMClient]):
    """
    RAM service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ram/)
    """
