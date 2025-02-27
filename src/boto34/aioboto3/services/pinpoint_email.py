"""
Wrapper for aioboto3 PinpointEmail service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pinpoint_email/)

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
    # Returns type annotated aioboto3 PinpointEmail client
    pinpoint_email_client = session.pinpoint_email.client()
    pinpoint_email_client: types_aiobotocore_pinpoint_email.client.PinpointEmailClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_pinpoint_email.client import PinpointEmailClient
except ImportError:
    PinpointEmailClient = object  # type: ignore[misc,assignment]


class PinpointEmailService(
    ServiceFactory[PinpointEmailClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "pinpoint-email"
    _SERVICE_PROP = "pinpoint_email"
