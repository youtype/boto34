"""
Wrapper for aioboto3 GroundStation service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_groundstation/)

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
    # Returns type annotated aioboto3 GroundStation client
    groundstation_client = session.groundstation.client()
    groundstation_client: types_aiobotocore_groundstation.client.GroundStationClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_groundstation.client import GroundStationClient

from boto34.aioboto3.service_factory import ServiceFactory


class GroundStationService(ServiceFactory[GroundStationClient]):
    SERVICE_NAME = "groundstation"
    _SERVICE_PROP = "groundstation"
