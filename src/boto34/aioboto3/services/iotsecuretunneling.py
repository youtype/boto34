"""
Wrapper for aioboto3 IoTSecureTunneling service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iotsecuretunneling/)

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
    # Returns type annotated aioboto3 IoTSecureTunneling client
    iotsecuretunneling_client = session.iotsecuretunneling.client()
    iotsecuretunneling_client: types_aiobotocore_iotsecuretunneling.client.IoTSecureTunnelingClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_iotsecuretunneling.client import IoTSecureTunnelingClient

from boto34.aioboto3.service_factory import ServiceFactory


class IoTSecureTunnelingService(ServiceFactory[IoTSecureTunnelingClient]):
    SERVICE_NAME = "iotsecuretunneling"
    _SERVICE_PROP = "iotsecuretunneling"
