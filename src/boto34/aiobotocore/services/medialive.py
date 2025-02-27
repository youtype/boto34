"""
Wrapper for aiobotocore MediaLive service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/)

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
    # Returns type annotated aiobotocore MediaLive client
    async with session.medialive.create_client() as medialive_client:
        medialive_client: types_aiobotocore_medialive.client.MediaLiveClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_medialive.client import MediaLiveClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MediaLiveService(ServiceFactory[MediaLiveClient]):
    SERVICE_NAME = "medialive"
    _SERVICE_PROP = "medialive"
