"""
Wrapper for aiobotocore ServiceCatalog service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_servicecatalog/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore ServiceCatalog client
    async with session.servicecatalog.create_client() as servicecatalog_client:
        servicecatalog_client: types_aiobotocore_servicecatalog.client.ServiceCatalogClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_servicecatalog.client import ServiceCatalogClient
except ImportError:
    ServiceCatalogClient = object  # type: ignore[misc,assignment]


class ServiceCatalogService(
    ServiceFactory[ServiceCatalogClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "servicecatalog"
    _SERVICE_PROP = "servicecatalog"
