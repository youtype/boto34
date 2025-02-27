"""
Wrapper for aiobotocore Private5G service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_privatenetworks/)

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
    # Returns type annotated aiobotocore Private5G client
    async with session.privatenetworks.create_client() as privatenetworks_client:
        privatenetworks_client: types_aiobotocore_privatenetworks.client.Private5GClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_privatenetworks.client import Private5GClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_privatenetworks.client import Private5GClient
except ImportError:
    Private5GClient = object  # type: ignore[misc,assignment]


class Private5GService(
    ServiceFactory[Private5GClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "privatenetworks"
    _SERVICE_PROP = "privatenetworks"
