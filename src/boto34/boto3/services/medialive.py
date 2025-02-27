"""
Wrapper for boto3 MediaLive service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_medialive/)

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
    # Returns type annotated boto3 MediaLive client
    medialive_client = session.medialive.client()
    medialive_client: types_boto3_medialive.client.MediaLiveClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_medialive.client import MediaLiveClient
except ImportError:
    MediaLiveClient = object  # type: ignore[misc,assignment]


class MediaLiveService(
    ServiceFactory[MediaLiveClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "medialive"
    _SERVICE_PROP = "medialive"
