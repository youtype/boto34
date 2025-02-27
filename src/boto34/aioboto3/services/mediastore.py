"""
Wrapper for aioboto3 MediaStore service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mediastore/)

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
    # Returns type annotated aioboto3 MediaStore client
    mediastore_client = session.mediastore.client()
    mediastore_client: types_aiobotocore_mediastore.client.MediaStoreClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_mediastore.client import MediaStoreClient
except ImportError:
    MediaStoreClient = object  # type: ignore[misc,assignment]


class MediaStoreService(
    ServiceFactory[MediaStoreClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "mediastore"
    _SERVICE_PROP = "mediastore"
