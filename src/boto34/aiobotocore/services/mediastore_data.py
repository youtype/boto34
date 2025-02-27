"""
Wrapper for aiobotocore MediaStoreData service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediastore_data/)

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
    # Returns type annotated aiobotocore MediaStoreData client
    async with session.mediastore_data.create_client() as mediastore_data_client:
        mediastore_data_client: types_aiobotocore_mediastore_data.client.MediaStoreDataClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_mediastore_data.client import MediaStoreDataClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MediaStoreDataService(ServiceFactory[MediaStoreDataClient]):
    SERVICE_NAME = "mediastore-data"
    _SERVICE_PROP = "mediastore_data"
