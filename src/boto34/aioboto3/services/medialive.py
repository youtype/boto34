"""
Wrapper for aioboto3 MediaLive service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_medialive/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_medialive.client import MediaLiveClient

from boto34.aioboto3.service_factory import ServiceFactory


class MediaLiveService(ServiceFactory[MediaLiveClient]):
    """
    MediaLive service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_medialive/)
    """
