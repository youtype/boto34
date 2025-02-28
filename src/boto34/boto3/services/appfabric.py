"""
Wrapper for boto3 AppFabric service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_appfabric/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_appfabric.client import AppFabricClient

from boto34.boto3.service_factory import ServiceFactory


class AppFabricService(ServiceFactory[AppFabricClient]):
    """
    AppFabric service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_appfabric/)
    """
