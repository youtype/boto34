"""
Wrapper for boto3 MediaPackageVod service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediapackage_vod/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 MediaPackageVod client
    mediapackage_vod_client = session.mediapackage_vod.client()
    mediapackage_vod_client: types_boto3_mediapackage_vod.client.MediaPackageVodClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_mediapackage_vod.client import MediaPackageVodClient
except ImportError:
    MediaPackageVodClient = object  # type: ignore[misc,assignment]


class MediaPackageVodService(
    ServiceFactory[MediaPackageVodClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "mediapackage-vod"
    _SERVICE_PROP = "mediapackage_vod"
