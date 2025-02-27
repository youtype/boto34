"""
Wrapper for aioboto3 CleanRoomsService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cleanrooms/)

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
    # Returns type annotated aioboto3 CleanRoomsService client
    cleanrooms_client = session.cleanrooms.client()
    cleanrooms_client: types_aiobotocore_cleanrooms.client.CleanRoomsServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_cleanrooms.client import CleanRoomsServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class CleanRoomsServiceService(ServiceFactory[CleanRoomsServiceClient]):
    SERVICE_NAME = "cleanrooms"
    _SERVICE_PROP = "cleanrooms"
