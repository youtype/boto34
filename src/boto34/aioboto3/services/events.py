"""
Wrapper for aioboto3 EventBridge service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_events/)

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
    # Returns type annotated aioboto3 EventBridge client
    events_client = session.events.client()
    events_client: types_aiobotocore_events.client.EventBridgeClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_events.client import EventBridgeClient

from boto34.aioboto3.service_factory import ServiceFactory


class EventBridgeService(ServiceFactory[EventBridgeClient]):
    SERVICE_NAME = "events"
    _SERVICE_PROP = "events"
