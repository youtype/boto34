"""
Wrapper for aioboto3 RoboMaker service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_robomaker/)

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
    # Returns type annotated aioboto3 RoboMaker client
    robomaker_client = session.robomaker.client()
    robomaker_client: types_aiobotocore_robomaker.client.RoboMakerClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_robomaker.client import RoboMakerClient
except ImportError:
    RoboMakerClient = object  # type: ignore[misc,assignment]


class RoboMakerService(
    ServiceFactory[RoboMakerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "robomaker"
    _SERVICE_PROP = "robomaker"
