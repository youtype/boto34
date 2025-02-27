"""
Wrapper for boto3 EventBridge service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_events/)

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
    # Returns type annotated boto3 EventBridge client
    events_client = session.events.client()
    events_client: types_boto3_events.client.EventBridgeClient
    ```
"""

from __future__ import annotations

from types_boto3_events.client import EventBridgeClient

from boto34.boto3.service_factory import ServiceFactory


class EventBridgeService(ServiceFactory[EventBridgeClient]):
    SERVICE_NAME = "events"
    _SERVICE_PROP = "events"
