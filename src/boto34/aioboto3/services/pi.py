"""
Wrapper for aioboto3 PI service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pi/)

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
    # Returns type annotated aioboto3 PI client
    pi_client = session.pi.client()
    pi_client: types_aiobotocore_pi.client.PIClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_pi.client import PIClient
except ImportError:
    PIClient = object  # type: ignore[misc,assignment]


class PIService(
    ServiceFactory[PIClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "pi"
    _SERVICE_PROP = "pi"
