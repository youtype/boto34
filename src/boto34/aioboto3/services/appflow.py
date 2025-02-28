"""
Wrapper for aioboto3 Appflow service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appflow/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_appflow.client import AppflowClient

from boto34.aioboto3.service_factory import ServiceFactory


class AppflowService(ServiceFactory[AppflowClient]):
    """
    Appflow service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appflow/)
    """
