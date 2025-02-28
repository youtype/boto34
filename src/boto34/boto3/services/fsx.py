"""
Wrapper for boto3 FSx service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_fsx/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_fsx.client import FSxClient

from boto34.boto3.service_factory import ServiceFactory


class FSxService(ServiceFactory[FSxClient]):
    """
    FSx service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_fsx/)
    """
