"""
Wrapper for aiobotocore EventBridge service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/)

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
    # Returns type annotated aiobotocore EventBridge client
    async with session.events.create_client() as events_client:
        events_client: types_aiobotocore_events.client.EventBridgeClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_events.client import EventBridgeClient

from boto34.aiobotocore.service_factory import ServiceFactory


class EventBridgeService(ServiceFactory[EventBridgeClient]):
    SERVICE_NAME = "events"
    _SERVICE_PROP = "events"
