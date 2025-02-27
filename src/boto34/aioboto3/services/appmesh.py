"""
Wrapper for aioboto3 AppMesh service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appmesh/)

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
    # Returns type annotated aioboto3 AppMesh client
    appmesh_client = session.appmesh.client()
    appmesh_client: types_aiobotocore_appmesh.client.AppMeshClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_appmesh.client import AppMeshClient
except ImportError:
    AppMeshClient = object  # type: ignore[misc,assignment]


class AppMeshService(
    ServiceFactory[AppMeshClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "appmesh"
    _SERVICE_PROP = "appmesh"
