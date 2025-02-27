"""
Wrapper for aiobotocore Finspace service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/)

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
    # Returns type annotated aiobotocore Finspace client
    async with session.finspace.create_client() as finspace_client:
        finspace_client: types_aiobotocore_finspace.client.FinspaceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_finspace.client import FinspaceClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_finspace.client import FinspaceClient
except ImportError:
    FinspaceClient = object  # type: ignore[misc,assignment]


class FinspaceService(
    ServiceFactory[FinspaceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "finspace"
    _SERVICE_PROP = "finspace"
