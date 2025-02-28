"""
Wrapper for boto3 KinesisVideo service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesisvideo/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_kinesisvideo.client import KinesisVideoClient

from boto34.boto3.service_factory import ServiceFactory


class KinesisVideoService(ServiceFactory[KinesisVideoClient]):
    """
    KinesisVideo service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesisvideo/)
    """
