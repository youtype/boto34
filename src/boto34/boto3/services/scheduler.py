"""
Wrapper for boto3 EventBridgeScheduler service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_scheduler/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_scheduler.client import EventBridgeSchedulerClient

from boto34.boto3.service_factory import ServiceFactory


class EventBridgeSchedulerService(ServiceFactory[EventBridgeSchedulerClient]):
    """
    EventBridgeScheduler service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_scheduler/)
    """
