"""
Wrapper for aiobotocore ChimeSDKMediaPipelines service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore ChimeSDKMediaPipelines client
    async with session.chime_sdk_media_pipelines.create_client() as chime_sdk_media_pipelines_client:
        chime_sdk_media_pipelines_client: (
            types_aiobotocore_chime_sdk_media_pipelines.client.ChimeSDKMediaPipelinesClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_chime_sdk_media_pipelines.client import ChimeSDKMediaPipelinesClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_chime_sdk_media_pipelines.client import ChimeSDKMediaPipelinesClient
except ImportError:
    ChimeSDKMediaPipelinesClient = object  # type: ignore[misc,assignment]


class ChimeSDKMediaPipelinesService(
    ServiceFactory[ChimeSDKMediaPipelinesClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "chime-sdk-media-pipelines"
    _SERVICE_PROP = "chime_sdk_media_pipelines"
