"""
Wrapper for boto3 IVS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ivs/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_ivs.client import IVSClient

from boto34.boto3.service_factory import ServiceFactory


class IVSService(ServiceFactory[IVSClient]):
    """
    IVS service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ivs/)
    """
