"""
Wrapper for aiobotocore AppConfig service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/)

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
    # Returns type annotated aiobotocore AppConfig client
    async with session.appconfig.create_client() as appconfig_client:
        appconfig_client: types_aiobotocore_appconfig.client.AppConfigClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_appconfig.client import AppConfigClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_appconfig.client import AppConfigClient
except ImportError:
    AppConfigClient = object  # type: ignore[misc,assignment]


class AppConfigService(
    ServiceFactory[AppConfigClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "appconfig"
    _SERVICE_PROP = "appconfig"
