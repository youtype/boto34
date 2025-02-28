"""
Wrapper for boto3 ChimeSDKMediaPipelines service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_chime_sdk_media_pipelines/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_chime_sdk_media_pipelines.client import ChimeSDKMediaPipelinesClient

from boto34.boto3.service_factory import ServiceFactory


class ChimeSDKMediaPipelinesService(ServiceFactory[ChimeSDKMediaPipelinesClient]):
    """
    ChimeSDKMediaPipelines service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_chime_sdk_media_pipelines/)
    """
