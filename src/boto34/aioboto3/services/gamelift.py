"""
Wrapper for aioboto3 GameLift service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_gamelift/)

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
    # Returns type annotated aioboto3 GameLift client
    gamelift_client = session.gamelift.client()
    gamelift_client: types_aiobotocore_gamelift.client.GameLiftClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_gamelift.client import GameLiftClient
except ImportError:
    GameLiftClient = object  # type: ignore[misc,assignment]


class GameLiftService(
    ServiceFactory[GameLiftClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "gamelift"
    _SERVICE_PROP = "gamelift"
