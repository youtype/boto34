"""
Wrapper for aiobotocore EventBridgePipes service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/)

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
    # Returns type annotated aiobotocore EventBridgePipes client
    async with session.pipes.create_client() as pipes_client:
        pipes_client: types_aiobotocore_pipes.client.EventBridgePipesClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_pipes.client import EventBridgePipesClient
except ImportError:
    EventBridgePipesClient = object  # type: ignore[misc,assignment]


class EventBridgePipesService(
    ServiceFactory[EventBridgePipesClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "pipes"
    _SERVICE_PROP = "pipes"
