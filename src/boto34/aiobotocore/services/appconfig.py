"""
Wrapper for aiobotocore AppConfig service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_appconfig.client import AppConfigClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AppConfigService(ServiceFactory[AppConfigClient]):
    """
    AppConfig service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/)
    """
