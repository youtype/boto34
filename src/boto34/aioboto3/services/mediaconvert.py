"""
Wrapper for aioboto3 MediaConvert service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mediaconvert/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_mediaconvert.client import MediaConvertClient

from boto34.aioboto3.service_factory import ServiceFactory


class MediaConvertService(ServiceFactory[MediaConvertClient]):
    """
    MediaConvert service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mediaconvert/)
    """
