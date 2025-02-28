"""
Wrapper for aiobotocore AppConfigData service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfigdata/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_appconfigdata.client import AppConfigDataClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AppConfigDataService(ServiceFactory[AppConfigDataClient]):
    """
    AppConfigData service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfigdata/)
    """
