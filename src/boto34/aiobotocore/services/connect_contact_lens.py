"""
Wrapper for aiobotocore ConnectContactLens service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect_contact_lens/)

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
    # Returns type annotated aiobotocore ConnectContactLens client
    async with session.connect_contact_lens.create_client() as connect_contact_lens_client:
        connect_contact_lens_client: (
            types_aiobotocore_connect_contact_lens.client.ConnectContactLensClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_connect_contact_lens.client import ConnectContactLensClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_connect_contact_lens.client import ConnectContactLensClient
except ImportError:
    ConnectContactLensClient = object  # type: ignore[misc,assignment]


class ConnectContactLensService(
    ServiceFactory[ConnectContactLensClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "connect-contact-lens"
    _SERVICE_PROP = "connect_contact_lens"
