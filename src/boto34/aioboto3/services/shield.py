"""
Wrapper for aioboto3 Shield service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_shield/)

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
    # Returns type annotated aioboto3 Shield client
    shield_client = session.shield.client()
    shield_client: types_aiobotocore_shield.client.ShieldClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_shield.client import ShieldClient
except ImportError:
    ShieldClient = object  # type: ignore[misc,assignment]


class ShieldService(
    ServiceFactory[ShieldClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "shield"
    _SERVICE_PROP = "shield"
