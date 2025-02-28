"""
Wrapper for aiobotocore AppRegistry service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_servicecatalog_appregistry/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_servicecatalog_appregistry.client import AppRegistryClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AppRegistryService(ServiceFactory[AppRegistryClient]):
    """
    AppRegistry service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_servicecatalog_appregistry/)
    """
