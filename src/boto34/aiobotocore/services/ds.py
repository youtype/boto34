"""
Wrapper for aiobotocore DirectoryService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ds/)

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
    # Returns type annotated aiobotocore DirectoryService client
    async with session.ds.create_client() as ds_client:
        ds_client: types_aiobotocore_ds.client.DirectoryServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_ds.client import DirectoryServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_ds.client import DirectoryServiceClient
except ImportError:
    DirectoryServiceClient = object  # type: ignore[misc,assignment]


class DirectoryServiceService(
    ServiceFactory[DirectoryServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ds"
    _SERVICE_PROP = "ds"
