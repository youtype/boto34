"""
Wrapper for boto3 MediaLive service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_medialive/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_medialive.client import MediaLiveClient

from boto34.boto3.service_factory import ServiceFactory


class MediaLiveService(ServiceFactory[MediaLiveClient]):
    """
    MediaLive service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_medialive/)
    """
