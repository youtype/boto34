"""
Wrapper for aioboto3 EventBridgePipes service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pipes/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 EventBridgePipes client
    pipes_client = session.pipes.client()
    pipes_client: types_aiobotocore_pipes.client.EventBridgePipesClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_pipes.client import EventBridgePipesClient

from boto34.aioboto3.service_factory import ServiceFactory


class EventBridgePipesService(ServiceFactory[EventBridgePipesClient]):
    SERVICE_NAME = "pipes"
    _SERVICE_PROP = "pipes"
