"""
Wrapper for aiobotocore Outposts service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_outposts/)

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
    # Returns type annotated aiobotocore Outposts client
    async with session.outposts.create_client() as outposts_client:
        outposts_client: types_aiobotocore_outposts.client.OutpostsClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_outposts.client import OutpostsClient
except ImportError:
    OutpostsClient = object  # type: ignore[misc,assignment]


class OutpostsService(
    ServiceFactory[OutpostsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "outposts"
    _SERVICE_PROP = "outposts"
