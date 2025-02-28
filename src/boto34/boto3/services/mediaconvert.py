"""
Wrapper for boto3 MediaConvert service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediaconvert/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_mediaconvert.client import MediaConvertClient

from boto34.boto3.service_factory import ServiceFactory


class MediaConvertService(ServiceFactory[MediaConvertClient]):
    """
    MediaConvert service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediaconvert/)
    """
