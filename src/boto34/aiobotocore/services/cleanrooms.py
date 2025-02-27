"""
Wrapper for aiobotocore CleanRoomsService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cleanrooms/)

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
    # Returns type annotated aiobotocore CleanRoomsService client
    async with session.cleanrooms.create_client() as cleanrooms_client:
        cleanrooms_client: types_aiobotocore_cleanrooms.client.CleanRoomsServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_cleanrooms.client import CleanRoomsServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_cleanrooms.client import CleanRoomsServiceClient
except ImportError:
    CleanRoomsServiceClient = object  # type: ignore[misc,assignment]


class CleanRoomsServiceService(
    ServiceFactory[CleanRoomsServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cleanrooms"
    _SERVICE_PROP = "cleanrooms"
