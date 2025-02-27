"""
Wrapper for boto3 GameLift service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_gamelift/)

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
    # Returns type annotated boto3 GameLift client
    gamelift_client = session.gamelift.client()
    gamelift_client: types_boto3_gamelift.client.GameLiftClient
    ```
"""

from __future__ import annotations

from types_boto3_gamelift.client import GameLiftClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_gamelift.client import GameLiftClient
except ImportError:
    GameLiftClient = object  # type: ignore[misc,assignment]


class GameLiftService(
    ServiceFactory[GameLiftClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "gamelift"
    _SERVICE_PROP = "gamelift"
