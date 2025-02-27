"""
Wrapper for boto3 MediaPackage service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediapackage/)

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
    # Returns type annotated boto3 MediaPackage client
    mediapackage_client = session.mediapackage.client()
    mediapackage_client: types_boto3_mediapackage.client.MediaPackageClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_mediapackage.client import MediaPackageClient
except ImportError:
    MediaPackageClient = object  # type: ignore[misc,assignment]


class MediaPackageService(
    ServiceFactory[MediaPackageClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "mediapackage"
    _SERVICE_PROP = "mediapackage"
