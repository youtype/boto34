"""
Wrapper for aiobotocore CleanRoomsML service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cleanroomsml/)

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
    # Returns type annotated aiobotocore CleanRoomsML client
    async with session.cleanroomsml.create_client() as cleanroomsml_client:
        cleanroomsml_client: types_aiobotocore_cleanroomsml.client.CleanRoomsMLClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_cleanroomsml.client import CleanRoomsMLClient
except ImportError:
    CleanRoomsMLClient = object  # type: ignore[misc,assignment]


class CleanRoomsMLService(
    ServiceFactory[CleanRoomsMLClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cleanroomsml"
    _SERVICE_PROP = "cleanroomsml"
