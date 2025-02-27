"""
Wrapper for aioboto3 ControlTower service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_controltower/)

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
    # Returns type annotated aioboto3 ControlTower client
    controltower_client = session.controltower.client()
    controltower_client: types_aiobotocore_controltower.client.ControlTowerClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_controltower.client import ControlTowerClient
except ImportError:
    ControlTowerClient = object  # type: ignore[misc,assignment]


class ControlTowerService(
    ServiceFactory[ControlTowerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "controltower"
    _SERVICE_PROP = "controltower"
