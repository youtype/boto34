"""
Wrapper for aiobotocore MediaTailor service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/)

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
    # Returns type annotated aiobotocore MediaTailor client
    async with session.mediatailor.create_client() as mediatailor_client:
        mediatailor_client: types_aiobotocore_mediatailor.client.MediaTailorClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_mediatailor.client import MediaTailorClient
except ImportError:
    MediaTailorClient = object  # type: ignore[misc,assignment]


class MediaTailorService(
    ServiceFactory[MediaTailorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "mediatailor"
    _SERVICE_PROP = "mediatailor"
