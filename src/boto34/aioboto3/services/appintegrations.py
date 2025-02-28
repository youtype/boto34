"""
Wrapper for aioboto3 AppIntegrationsService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appintegrations/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_appintegrations.client import AppIntegrationsServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class AppIntegrationsServiceService(ServiceFactory[AppIntegrationsServiceClient]):
    """
    AppIntegrationsService service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appintegrations/)
    """
