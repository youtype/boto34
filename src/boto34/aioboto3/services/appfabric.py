"""
Wrapper for aioboto3 AppFabric service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appfabric/)

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
    # Returns type annotated aioboto3 AppFabric client
    appfabric_client = session.appfabric.client()
    appfabric_client: types_aiobotocore_appfabric.client.AppFabricClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_appfabric.client import AppFabricClient
except ImportError:
    AppFabricClient = object  # type: ignore[misc,assignment]


class AppFabricService(
    ServiceFactory[AppFabricClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "appfabric"
    _SERVICE_PROP = "appfabric"
