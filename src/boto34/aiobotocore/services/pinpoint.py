"""
Wrapper for aiobotocore Pinpoint service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint/)

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
    # Returns type annotated aiobotocore Pinpoint client
    async with session.pinpoint.create_client() as pinpoint_client:
        pinpoint_client: types_aiobotocore_pinpoint.client.PinpointClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_pinpoint.client import PinpointClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_pinpoint.client import PinpointClient
except ImportError:
    PinpointClient = object  # type: ignore[misc,assignment]


class PinpointService(
    ServiceFactory[PinpointClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "pinpoint"
    _SERVICE_PROP = "pinpoint"
