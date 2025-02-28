"""
Wrapper for aiobotocore MediaPackageVod service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediapackage_vod/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_mediapackage_vod.client import MediaPackageVodClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MediaPackageVodService(ServiceFactory[MediaPackageVodClient]):
    """
    MediaPackageVod service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediapackage_vod/)
    """
