"""
Wrapper for aiobotocore AppIntegrationsService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_appintegrations.client import AppIntegrationsServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AppIntegrationsServiceService(ServiceFactory[AppIntegrationsServiceClient]):
    """
    AppIntegrationsService service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/)
    """
