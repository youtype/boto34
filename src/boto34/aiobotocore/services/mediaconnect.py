"""
Wrapper for aiobotocore MediaConnect service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/)

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
    # Returns type annotated aiobotocore MediaConnect client
    async with session.mediaconnect.create_client() as mediaconnect_client:
        mediaconnect_client: types_aiobotocore_mediaconnect.client.MediaConnectClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_mediaconnect.client import MediaConnectClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MediaConnectService(ServiceFactory[MediaConnectClient]):
    SERVICE_NAME = "mediaconnect"
    _SERVICE_PROP = "mediaconnect"
