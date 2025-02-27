"""
Wrapper for aioboto3 MediaStoreData service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mediastore_data/)

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
    # Returns type annotated aioboto3 MediaStoreData client
    mediastore_data_client = session.mediastore_data.client()
    mediastore_data_client: types_aiobotocore_mediastore_data.client.MediaStoreDataClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_mediastore_data.client import MediaStoreDataClient
except ImportError:
    MediaStoreDataClient = object  # type: ignore[misc,assignment]


class MediaStoreDataService(
    ServiceFactory[MediaStoreDataClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "mediastore-data"
    _SERVICE_PROP = "mediastore_data"
