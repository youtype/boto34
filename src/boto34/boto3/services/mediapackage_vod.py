"""
Wrapper for boto3 MediaPackageVod service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediapackage_vod/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_mediapackage_vod.client import MediaPackageVodClient

from boto34.boto3.service_factory import ServiceFactory


class MediaPackageVodService(ServiceFactory[MediaPackageVodClient]):
    """
    MediaPackageVod service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediapackage_vod/)
    """
