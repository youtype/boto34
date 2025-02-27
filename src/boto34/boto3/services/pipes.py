"""
Wrapper for boto3 EventBridgePipes service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pipes/)

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
    # Returns type annotated boto3 EventBridgePipes client
    pipes_client = session.pipes.client()
    pipes_client: types_boto3_pipes.client.EventBridgePipesClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_pipes.client import EventBridgePipesClient
except ImportError:
    EventBridgePipesClient = object  # type: ignore[misc,assignment]


class EventBridgePipesService(
    ServiceFactory[EventBridgePipesClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "pipes"
    _SERVICE_PROP = "pipes"
