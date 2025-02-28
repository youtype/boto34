"""
Wrapper for aioboto3 EventBridgePipes service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pipes/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_pipes.client import EventBridgePipesClient

from boto34.aioboto3.service_factory import ServiceFactory


class EventBridgePipesService(ServiceFactory[EventBridgePipesClient]):
    """
    EventBridgePipes service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pipes/)
    """
