"""
Wrapper for aioboto3 AppSync service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appsync/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_appsync.client import AppSyncClient

from boto34.aioboto3.service_factory import ServiceFactory


class AppSyncService(ServiceFactory[AppSyncClient]):
    """
    AppSync service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appsync/)
    """
