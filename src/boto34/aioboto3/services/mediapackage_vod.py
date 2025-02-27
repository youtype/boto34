"""
Wrapper for aioboto3 MediaPackageVod service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mediapackage_vod/)

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
    # Returns type annotated aioboto3 MediaPackageVod client
    mediapackage_vod_client = session.mediapackage_vod.client()
    mediapackage_vod_client: types_aiobotocore_mediapackage_vod.client.MediaPackageVodClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_mediapackage_vod.client import MediaPackageVodClient

from boto34.aioboto3.service_factory import ServiceFactory


class MediaPackageVodService(ServiceFactory[MediaPackageVodClient]):
    SERVICE_NAME = "mediapackage-vod"
    _SERVICE_PROP = "mediapackage_vod"
