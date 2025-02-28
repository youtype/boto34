"""
Wrapper for aioboto3 MediaPackageVod service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mediapackage_vod/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_mediapackage_vod.client import MediaPackageVodClient

from boto34.aioboto3.service_factory import ServiceFactory


class MediaPackageVodService(ServiceFactory[MediaPackageVodClient]):
    """
    MediaPackageVod service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mediapackage_vod/)
    """
