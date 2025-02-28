"""
Wrapper for boto3 DirectConnect service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_directconnect/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_directconnect.client import DirectConnectClient

from boto34.boto3.service_factory import ServiceFactory


class DirectConnectService(ServiceFactory[DirectConnectClient]):
    """
    DirectConnect service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_directconnect/)
    """
