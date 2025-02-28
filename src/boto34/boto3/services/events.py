"""
Wrapper for boto3 EventBridge service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_events/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_events.client import EventBridgeClient

from boto34.boto3.service_factory import ServiceFactory


class EventBridgeService(ServiceFactory[EventBridgeClient]):
    """
    EventBridge service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_events/)
    """
