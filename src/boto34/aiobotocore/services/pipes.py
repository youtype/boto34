"""
Wrapper for aiobotocore EventBridgePipes service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_pipes.client import EventBridgePipesClient

from boto34.aiobotocore.service_factory import ServiceFactory


class EventBridgePipesService(ServiceFactory[EventBridgePipesClient]):
    """
    EventBridgePipes service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/)
    """
