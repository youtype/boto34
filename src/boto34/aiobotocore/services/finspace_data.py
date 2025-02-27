"""
Wrapper for aiobotocore FinSpaceData service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace_data/)

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
    # Returns type annotated aiobotocore FinSpaceData client
    async with session.finspace_data.create_client() as finspace_data_client:
        finspace_data_client: types_aiobotocore_finspace_data.client.FinSpaceDataClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_finspace_data.client import FinSpaceDataClient
except ImportError:
    FinSpaceDataClient = object  # type: ignore[misc,assignment]


class FinSpaceDataService(
    ServiceFactory[FinSpaceDataClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "finspace-data"
    _SERVICE_PROP = "finspace_data"
