"""
Wrapper for boto3 ChimeSDKMediaPipelines service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_chime_sdk_media_pipelines/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 ChimeSDKMediaPipelines client
    chime_sdk_media_pipelines_client = session.chime_sdk_media_pipelines.client()
    chime_sdk_media_pipelines_client: (
        types_boto3_chime_sdk_media_pipelines.client.ChimeSDKMediaPipelinesClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_chime_sdk_media_pipelines.client import ChimeSDKMediaPipelinesClient

from boto34.boto3.service_factory import ServiceFactory


class ChimeSDKMediaPipelinesService(ServiceFactory[ChimeSDKMediaPipelinesClient]):
    SERVICE_NAME = "chime-sdk-media-pipelines"
    _SERVICE_PROP = "chime_sdk_media_pipelines"
