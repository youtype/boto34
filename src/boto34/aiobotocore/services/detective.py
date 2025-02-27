"""
Wrapper for aiobotocore Detective service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_detective/)

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
    # Returns type annotated aiobotocore Detective client
    async with session.detective.create_client() as detective_client:
        detective_client: types_aiobotocore_detective.client.DetectiveClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_detective.client import DetectiveClient
except ImportError:
    DetectiveClient = object  # type: ignore[misc,assignment]


class DetectiveService(
    ServiceFactory[DetectiveClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "detective"
    _SERVICE_PROP = "detective"
