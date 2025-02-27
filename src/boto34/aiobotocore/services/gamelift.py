"""
Wrapper for aiobotocore GameLift service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_gamelift/)

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
    # Returns type annotated aiobotocore GameLift client
    async with session.gamelift.create_client() as gamelift_client:
        gamelift_client: types_aiobotocore_gamelift.client.GameLiftClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_gamelift.client import GameLiftClient
except ImportError:
    GameLiftClient = object  # type: ignore[misc,assignment]


class GameLiftService(
    ServiceFactory[GameLiftClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "gamelift"
    _SERVICE_PROP = "gamelift"
