"""
Wrapper for aiobotocore CloudDirectory service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_clouddirectory/)

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
    # Returns type annotated aiobotocore CloudDirectory client
    async with session.clouddirectory.create_client() as clouddirectory_client:
        clouddirectory_client: types_aiobotocore_clouddirectory.client.CloudDirectoryClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_clouddirectory.client import CloudDirectoryClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_clouddirectory.client import CloudDirectoryClient
except ImportError:
    CloudDirectoryClient = object  # type: ignore[misc,assignment]


class CloudDirectoryService(
    ServiceFactory[CloudDirectoryClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "clouddirectory"
    _SERVICE_PROP = "clouddirectory"
