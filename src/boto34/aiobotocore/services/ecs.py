"""
Wrapper for aiobotocore ECS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ecs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore ECS client
    async with session.ecs.create_client() as ecs_client:
        ecs_client: types_aiobotocore_ecs.client.ECSClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_ecs.client import ECSClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_ecs.client import ECSClient
except ImportError:
    ECSClient = object  # type: ignore[misc,assignment]


class ECSService(
    ServiceFactory[ECSClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ecs"
    _SERVICE_PROP = "ecs"
