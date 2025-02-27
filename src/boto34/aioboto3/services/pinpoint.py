"""
Wrapper for aioboto3 Pinpoint service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pinpoint/)

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
    # Returns type annotated aioboto3 Pinpoint client
    pinpoint_client = session.pinpoint.client()
    pinpoint_client: types_aiobotocore_pinpoint.client.PinpointClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_pinpoint.client import PinpointClient
except ImportError:
    PinpointClient = object  # type: ignore[misc,assignment]


class PinpointService(
    ServiceFactory[PinpointClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "pinpoint"
    _SERVICE_PROP = "pinpoint"
