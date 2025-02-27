"""
Wrapper for aioboto3 WellArchitected service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_wellarchitected/)

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
    # Returns type annotated aioboto3 WellArchitected client
    wellarchitected_client = session.wellarchitected.client()
    wellarchitected_client: types_aiobotocore_wellarchitected.client.WellArchitectedClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_wellarchitected.client import WellArchitectedClient
except ImportError:
    WellArchitectedClient = object  # type: ignore[misc,assignment]


class WellArchitectedService(
    ServiceFactory[WellArchitectedClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "wellarchitected"
    _SERVICE_PROP = "wellarchitected"
