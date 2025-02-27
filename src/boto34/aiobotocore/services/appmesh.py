"""
Wrapper for aiobotocore AppMesh service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appmesh/)

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
    # Returns type annotated aiobotocore AppMesh client
    async with session.appmesh.create_client() as appmesh_client:
        appmesh_client: types_aiobotocore_appmesh.client.AppMeshClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_appmesh.client import AppMeshClient
except ImportError:
    AppMeshClient = object  # type: ignore[misc,assignment]


class AppMeshService(
    ServiceFactory[AppMeshClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "appmesh"
    _SERVICE_PROP = "appmesh"
