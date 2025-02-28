"""
Wrapper for aiobotocore AppRunner service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_apprunner.client import AppRunnerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AppRunnerService(ServiceFactory[AppRunnerClient]):
    """
    AppRunner service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/)
    """
