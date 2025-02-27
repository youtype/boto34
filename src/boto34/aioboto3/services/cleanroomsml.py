"""
Wrapper for aioboto3 CleanRoomsML service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cleanroomsml/)

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
    # Returns type annotated aioboto3 CleanRoomsML client
    cleanroomsml_client = session.cleanroomsml.client()
    cleanroomsml_client: types_aiobotocore_cleanroomsml.client.CleanRoomsMLClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_cleanroomsml.client import CleanRoomsMLClient

from boto34.aioboto3.service_factory import ServiceFactory


class CleanRoomsMLService(ServiceFactory[CleanRoomsMLClient]):
    SERVICE_NAME = "cleanroomsml"
    _SERVICE_PROP = "cleanroomsml"
