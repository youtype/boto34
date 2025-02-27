"""
Wrapper for boto3 MediaTailor service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediatailor/)

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
    # Returns type annotated boto3 MediaTailor client
    mediatailor_client = session.mediatailor.client()
    mediatailor_client: types_boto3_mediatailor.client.MediaTailorClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_mediatailor.client import MediaTailorClient
except ImportError:
    MediaTailorClient = object  # type: ignore[misc,assignment]


class MediaTailorService(
    ServiceFactory[MediaTailorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "mediatailor"
    _SERVICE_PROP = "mediatailor"
