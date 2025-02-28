"""
Wrapper for aiobotocore EventBridge service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_events.client import EventBridgeClient

from boto34.aiobotocore.service_factory import ServiceFactory


class EventBridgeService(ServiceFactory[EventBridgeClient]):
    """
    EventBridge service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/)
    """
