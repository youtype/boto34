"""
Wrapper for aioboto3 EventBridgeScheduler service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_scheduler/)

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
    # Returns type annotated aioboto3 EventBridgeScheduler client
    scheduler_client = session.scheduler.client()
    scheduler_client: types_aiobotocore_scheduler.client.EventBridgeSchedulerClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_scheduler.client import EventBridgeSchedulerClient
except ImportError:
    EventBridgeSchedulerClient = object  # type: ignore[misc,assignment]


class EventBridgeSchedulerService(
    ServiceFactory[EventBridgeSchedulerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "scheduler"
    _SERVICE_PROP = "scheduler"
