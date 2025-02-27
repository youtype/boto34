"""
Wrapper for aiobotocore RoboMaker service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_robomaker/)

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
    # Returns type annotated aiobotocore RoboMaker client
    async with session.robomaker.create_client() as robomaker_client:
        robomaker_client: types_aiobotocore_robomaker.client.RoboMakerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_robomaker.client import RoboMakerClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_robomaker.client import RoboMakerClient
except ImportError:
    RoboMakerClient = object  # type: ignore[misc,assignment]


class RoboMakerService(
    ServiceFactory[RoboMakerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "robomaker"
    _SERVICE_PROP = "robomaker"
