"""
Wrapper for aiobotocore AppRunner service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/)

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
    # Returns type annotated aiobotocore AppRunner client
    async with session.apprunner.create_client() as apprunner_client:
        apprunner_client: types_aiobotocore_apprunner.client.AppRunnerClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_apprunner.client import AppRunnerClient
except ImportError:
    AppRunnerClient = object  # type: ignore[misc,assignment]


class AppRunnerService(
    ServiceFactory[AppRunnerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "apprunner"
    _SERVICE_PROP = "apprunner"
