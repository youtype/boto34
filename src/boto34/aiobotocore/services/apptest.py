"""
Wrapper for aiobotocore MainframeModernizationApplicationTesting service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apptest/)

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
    # Returns type annotated aiobotocore MainframeModernizationApplicationTesting client
    async with session.apptest.create_client() as apptest_client:
        apptest_client: types_aiobotocore_apptest.client.MainframeModernizationApplicationTestingClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_apptest.client import MainframeModernizationApplicationTestingClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_apptest.client import MainframeModernizationApplicationTestingClient
except ImportError:
    MainframeModernizationApplicationTestingClient = object  # type: ignore[misc,assignment]


class MainframeModernizationApplicationTestingService(
    ServiceFactory[MainframeModernizationApplicationTestingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "apptest"
    _SERVICE_PROP = "apptest"
