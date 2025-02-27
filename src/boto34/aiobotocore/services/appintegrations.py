"""
Wrapper for aiobotocore AppIntegrationsService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/)

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
    # Returns type annotated aiobotocore AppIntegrationsService client
    async with session.appintegrations.create_client() as appintegrations_client:
        appintegrations_client: types_aiobotocore_appintegrations.client.AppIntegrationsServiceClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_appintegrations.client import AppIntegrationsServiceClient
except ImportError:
    AppIntegrationsServiceClient = object  # type: ignore[misc,assignment]


class AppIntegrationsServiceService(
    ServiceFactory[AppIntegrationsServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "appintegrations"
    _SERVICE_PROP = "appintegrations"
