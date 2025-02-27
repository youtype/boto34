"""
Wrapper for aiobotocore RePostPrivate service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_repostspace/)

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
    # Returns type annotated aiobotocore RePostPrivate client
    async with session.repostspace.create_client() as repostspace_client:
        repostspace_client: types_aiobotocore_repostspace.client.RePostPrivateClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_repostspace.client import RePostPrivateClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_repostspace.client import RePostPrivateClient
except ImportError:
    RePostPrivateClient = object  # type: ignore[misc,assignment]


class RePostPrivateService(
    ServiceFactory[RePostPrivateClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "repostspace"
    _SERVICE_PROP = "repostspace"
