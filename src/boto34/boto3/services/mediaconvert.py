"""
Wrapper for boto3 MediaConvert service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediaconvert/)

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
    # Returns type annotated boto3 MediaConvert client
    mediaconvert_client = session.mediaconvert.client()
    mediaconvert_client: types_boto3_mediaconvert.client.MediaConvertClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_mediaconvert.client import MediaConvertClient
except ImportError:
    MediaConvertClient = object  # type: ignore[misc,assignment]


class MediaConvertService(
    ServiceFactory[MediaConvertClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "mediaconvert"
    _SERVICE_PROP = "mediaconvert"
