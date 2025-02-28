"""
Wrapper for boto3 MediaConnect service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediaconnect/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_mediaconnect.client import MediaConnectClient

from boto34.boto3.service_factory import ServiceFactory


class MediaConnectService(ServiceFactory[MediaConnectClient]):
    """
    MediaConnect service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediaconnect/)
    """
