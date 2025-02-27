"""
Wrapper for aiobotocore MediaConvert service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconvert/)

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
    # Returns type annotated aiobotocore MediaConvert client
    async with session.mediaconvert.create_client() as mediaconvert_client:
        mediaconvert_client: types_aiobotocore_mediaconvert.client.MediaConvertClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_mediaconvert.client import MediaConvertClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MediaConvertService(ServiceFactory[MediaConvertClient]):
    SERVICE_NAME = "mediaconvert"
    _SERVICE_PROP = "mediaconvert"
