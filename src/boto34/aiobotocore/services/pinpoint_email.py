"""
Wrapper for aiobotocore PinpointEmail service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_email/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore PinpointEmail client
    async with session.pinpoint_email.create_client() as pinpoint_email_client:
        pinpoint_email_client: types_aiobotocore_pinpoint_email.client.PinpointEmailClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_pinpoint_email.client import PinpointEmailClient
except ImportError:
    PinpointEmailClient = object  # type: ignore[misc,assignment]


class PinpointEmailService(
    ServiceFactory[PinpointEmailClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "pinpoint-email"
    _SERVICE_PROP = "pinpoint_email"
