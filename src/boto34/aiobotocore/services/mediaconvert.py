"""
Wrapper for aiobotocore MediaConvert service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconvert/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_mediaconvert.client import MediaConvertClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MediaConvertService(ServiceFactory[MediaConvertClient]):
    """
    MediaConvert service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconvert/)
    """
