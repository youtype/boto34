"""
Wrapper for boto3 NetworkManager service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_networkmanager/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_networkmanager.client import NetworkManagerClient

from boto34.boto3.service_factory import ServiceFactory


class NetworkManagerService(ServiceFactory[NetworkManagerClient]):
    """
    NetworkManager service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_networkmanager/)
    """
