"""
Wrapper for boto3 KinesisVideoArchivedMedia service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis_video_archived_media/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_kinesis_video_archived_media.client import KinesisVideoArchivedMediaClient

from boto34.boto3.service_factory import ServiceFactory


class KinesisVideoArchivedMediaService(ServiceFactory[KinesisVideoArchivedMediaClient]):
    """
    KinesisVideoArchivedMedia service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis_video_archived_media/)
    """
