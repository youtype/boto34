"""
Wrapper for aioboto3 AppConfig service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appconfig/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_appconfig.client import AppConfigClient

from boto34.aioboto3.service_factory import ServiceFactory


class AppConfigService(ServiceFactory[AppConfigClient]):
    """
    AppConfig service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appconfig/)
    """
