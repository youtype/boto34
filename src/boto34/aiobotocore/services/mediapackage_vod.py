"""
Wrapper for aiobotocore MediaPackageVod service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediapackage_vod/)

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
    # Returns type annotated aiobotocore MediaPackageVod client
    async with session.mediapackage_vod.create_client() as mediapackage_vod_client:
        mediapackage_vod_client: types_aiobotocore_mediapackage_vod.client.MediaPackageVodClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_mediapackage_vod.client import MediaPackageVodClient
except ImportError:
    MediaPackageVodClient = object  # type: ignore[misc,assignment]


class MediaPackageVodService(
    ServiceFactory[MediaPackageVodClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "mediapackage-vod"
    _SERVICE_PROP = "mediapackage_vod"
