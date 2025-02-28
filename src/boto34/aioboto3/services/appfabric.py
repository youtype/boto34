"""
Wrapper for aioboto3 AppFabric service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appfabric/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_appfabric.client import AppFabricClient

from boto34.aioboto3.service_factory import ServiceFactory


class AppFabricService(ServiceFactory[AppFabricClient]):
    """
    AppFabric service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appfabric/)
    """
