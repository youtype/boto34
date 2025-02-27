"""
Wrapper for aioboto3 ECS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ecs/)

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
    # Returns type annotated aioboto3 ECS client
    ecs_client = session.ecs.client()
    ecs_client: types_aiobotocore_ecs.client.ECSClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_ecs.client import ECSClient
except ImportError:
    ECSClient = object  # type: ignore[misc,assignment]


class ECSService(
    ServiceFactory[ECSClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ecs"
    _SERVICE_PROP = "ecs"
