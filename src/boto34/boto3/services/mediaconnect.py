"""
Wrapper for boto3 MediaConnect service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediaconnect/)

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
    # Returns type annotated boto3 MediaConnect client
    mediaconnect_client = session.mediaconnect.client()
    mediaconnect_client: types_boto3_mediaconnect.client.MediaConnectClient
    ```
"""

from __future__ import annotations

from types_boto3_mediaconnect.client import MediaConnectClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_mediaconnect.client import MediaConnectClient
except ImportError:
    MediaConnectClient = object  # type: ignore[misc,assignment]


class MediaConnectService(
    ServiceFactory[MediaConnectClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "mediaconnect"
    _SERVICE_PROP = "mediaconnect"
