"""
Wrapper for boto3 AppMesh service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_appmesh/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 AppMesh client
    appmesh_client = session.appmesh.client()
    appmesh_client: types_boto3_appmesh.client.AppMeshClient
    ```
"""

from __future__ import annotations

from types_boto3_appmesh.client import AppMeshClient

from boto34.boto3.service_factory import ServiceFactory


class AppMeshService(ServiceFactory[AppMeshClient]):
    SERVICE_NAME = "appmesh"
    _SERVICE_PROP = "appmesh"
