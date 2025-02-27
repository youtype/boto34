"""
Wrapper for aiobotocore EventBridgeScheduler service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_scheduler/)

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
    # Returns type annotated aiobotocore EventBridgeScheduler client
    async with session.scheduler.create_client() as scheduler_client:
        scheduler_client: types_aiobotocore_scheduler.client.EventBridgeSchedulerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_scheduler.client import EventBridgeSchedulerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class EventBridgeSchedulerService(ServiceFactory[EventBridgeSchedulerClient]):
    SERVICE_NAME = "scheduler"
    _SERVICE_PROP = "scheduler"
