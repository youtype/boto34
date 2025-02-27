"""
Wrapper for aiobotocore AppStream service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appstream/)

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
    # Returns type annotated aiobotocore AppStream client
    async with session.appstream.create_client() as appstream_client:
        appstream_client: types_aiobotocore_appstream.client.AppStreamClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_appstream.client import AppStreamClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_appstream.client import AppStreamClient
except ImportError:
    AppStreamClient = object  # type: ignore[misc,assignment]


class AppStreamService(
    ServiceFactory[AppStreamClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "appstream"
    _SERVICE_PROP = "appstream"
