"""
Wrapper for aioboto3 ChimeSDKMediaPipelines service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_chime_sdk_media_pipelines/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_chime_sdk_media_pipelines.client import ChimeSDKMediaPipelinesClient

from boto34.aioboto3.service_factory import ServiceFactory


class ChimeSDKMediaPipelinesService(ServiceFactory[ChimeSDKMediaPipelinesClient]):
    """
    ChimeSDKMediaPipelines service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_chime_sdk_media_pipelines/)
    """
