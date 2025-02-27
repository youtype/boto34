"""
Wrapper for aioboto3 Mediapackagev2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mediapackagev2/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 Mediapackagev2 client
    mediapackagev2_client = session.mediapackagev2.client()
    mediapackagev2_client: types_aiobotocore_mediapackagev2.client.Mediapackagev2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_mediapackagev2.client import Mediapackagev2Client

from boto34.aioboto3.service_factory import ServiceFactory


class Mediapackagev2Service(ServiceFactory[Mediapackagev2Client]):
    SERVICE_NAME = "mediapackagev2"
    _SERVICE_PROP = "mediapackagev2"
