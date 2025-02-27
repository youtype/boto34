"""
Wrapper for boto3 Mediapackagev2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediapackagev2/)

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
    # Returns type annotated boto3 Mediapackagev2 client
    mediapackagev2_client = session.mediapackagev2.client()
    mediapackagev2_client: types_boto3_mediapackagev2.client.Mediapackagev2Client
    ```
"""

from __future__ import annotations

from types_boto3_mediapackagev2.client import Mediapackagev2Client

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_mediapackagev2.client import Mediapackagev2Client
except ImportError:
    Mediapackagev2Client = object  # type: ignore[misc,assignment]


class Mediapackagev2Service(
    ServiceFactory[Mediapackagev2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "mediapackagev2"
    _SERVICE_PROP = "mediapackagev2"
