"""
Wrapper for aiobotocore MediaStore service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediastore/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore MediaStore client
    async with session.mediastore.create_client() as mediastore_client:
        mediastore_client: types_aiobotocore_mediastore.client.MediaStoreClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_mediastore.client import MediaStoreClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MediaStoreService(ServiceFactory[MediaStoreClient]):
    SERVICE_NAME = "mediastore"
    _SERVICE_PROP = "mediastore"
