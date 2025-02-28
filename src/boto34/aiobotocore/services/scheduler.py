"""
Wrapper for aiobotocore EventBridgeScheduler service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_scheduler/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_scheduler.client import EventBridgeSchedulerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class EventBridgeSchedulerService(ServiceFactory[EventBridgeSchedulerClient]):
    """
    EventBridgeScheduler service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_scheduler/)
    """
