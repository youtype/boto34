"""
Wrapper for boto3 EventBridgeScheduler service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_scheduler/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 EventBridgeScheduler client
    scheduler_client = session.scheduler.client()
    scheduler_client: types_boto3_scheduler.client.EventBridgeSchedulerClient
    ```
"""

from __future__ import annotations

from types_boto3_scheduler.client import EventBridgeSchedulerClient

from boto34.boto3.service_factory import ServiceFactory


class EventBridgeSchedulerService(ServiceFactory[EventBridgeSchedulerClient]):
    SERVICE_NAME = "scheduler"
    _SERVICE_PROP = "scheduler"
