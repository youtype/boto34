"""
Wrapper for aiobotocore ServiceCatalog service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_servicecatalog/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_servicecatalog.client import ServiceCatalogClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ServiceCatalogService(ServiceFactory[ServiceCatalogClient]):
    """
    ServiceCatalog service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_servicecatalog/)
    """
