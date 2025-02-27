"""
Wrapper for aiobotocore GroundStation service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_groundstation/)

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
    # Returns type annotated aiobotocore GroundStation client
    async with session.groundstation.create_client() as groundstation_client:
        groundstation_client: types_aiobotocore_groundstation.client.GroundStationClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_groundstation.client import GroundStationClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_groundstation.client import GroundStationClient
except ImportError:
    GroundStationClient = object  # type: ignore[misc,assignment]


class GroundStationService(
    ServiceFactory[GroundStationClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "groundstation"
    _SERVICE_PROP = "groundstation"
