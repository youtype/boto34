"""
Wrapper for boto3 Connect service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_connect/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_connect.client import ConnectClient

from boto34.boto3.service_factory import ServiceFactory


class ConnectService(ServiceFactory[ConnectClient]):
    """
    Connect service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_connect/)
    """
