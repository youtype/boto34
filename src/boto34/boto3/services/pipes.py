"""
Wrapper for boto3 EventBridgePipes service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pipes/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_pipes.client import EventBridgePipesClient

from boto34.boto3.service_factory import ServiceFactory


class EventBridgePipesService(ServiceFactory[EventBridgePipesClient]):
    """
    EventBridgePipes service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pipes/)
    """
