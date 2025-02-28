"""
Wrapper for aiobotocore KinesisVideoArchivedMedia service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesis_video_archived_media/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_kinesis_video_archived_media.client import KinesisVideoArchivedMediaClient

from boto34.aiobotocore.service_factory import ServiceFactory


class KinesisVideoArchivedMediaService(ServiceFactory[KinesisVideoArchivedMediaClient]):
    """
    KinesisVideoArchivedMedia service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesis_video_archived_media/)
    """
