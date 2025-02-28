"""
Wrapper for aioboto3 EventBridgeScheduler service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_scheduler/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_scheduler.client import EventBridgeSchedulerClient

from boto34.aioboto3.service_factory import ServiceFactory


class EventBridgeSchedulerService(ServiceFactory[EventBridgeSchedulerClient]):
    """
    EventBridgeScheduler service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_scheduler/)
    """
