"""
Wrapper for aiobotocore AppRegistry service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_servicecatalog_appregistry/)

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
    # Returns type annotated aiobotocore AppRegistry client
    async with session.servicecatalog_appregistry.create_client() as servicecatalog_appregistry_client:
        servicecatalog_appregistry_client: (
            types_aiobotocore_servicecatalog_appregistry.client.AppRegistryClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_servicecatalog_appregistry.client import AppRegistryClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_servicecatalog_appregistry.client import AppRegistryClient
except ImportError:
    AppRegistryClient = object  # type: ignore[misc,assignment]


class AppRegistryService(
    ServiceFactory[AppRegistryClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "servicecatalog-appregistry"
    _SERVICE_PROP = "servicecatalog_appregistry"
