"""
Wrapper for aioboto3 MediaConvert service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mediaconvert/)

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
    # Returns type annotated aioboto3 MediaConvert client
    mediaconvert_client = session.mediaconvert.client()
    mediaconvert_client: types_aiobotocore_mediaconvert.client.MediaConvertClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_mediaconvert.client import MediaConvertClient

from boto34.aioboto3.service_factory import ServiceFactory


class MediaConvertService(ServiceFactory[MediaConvertClient]):
    SERVICE_NAME = "mediaconvert"
    _SERVICE_PROP = "mediaconvert"
