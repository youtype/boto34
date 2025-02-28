"""
Wrapper for boto3 TelcoNetworkBuilder service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_tnb/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_tnb.client import TelcoNetworkBuilderClient

from boto34.boto3.service_factory import ServiceFactory


class TelcoNetworkBuilderService(ServiceFactory[TelcoNetworkBuilderClient]):
    """
    TelcoNetworkBuilder service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_tnb/)
    """
