"""
Wrapper for aioboto3 AppStream service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appstream/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 AppStream client
    appstream_client = session.appstream.client()
    appstream_client: types_aiobotocore_appstream.client.AppStreamClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_appstream.client import AppStreamClient
except ImportError:
    AppStreamClient = object  # type: ignore[misc,assignment]


class AppStreamService(
    ServiceFactory[AppStreamClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "appstream"
    _SERVICE_PROP = "appstream"
