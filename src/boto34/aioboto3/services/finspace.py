"""
Wrapper for aioboto3 Finspace service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_finspace/)

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
    # Returns type annotated aioboto3 Finspace client
    finspace_client = session.finspace.client()
    finspace_client: types_aiobotocore_finspace.client.FinspaceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_finspace.client import FinspaceClient

from boto34.aioboto3.service_factory import ServiceFactory


class FinspaceService(ServiceFactory[FinspaceClient]):
    SERVICE_NAME = "finspace"
    _SERVICE_PROP = "finspace"
