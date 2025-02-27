"""
Wrapper for aioboto3 MediaLive service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_medialive/)

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
    # Returns type annotated aioboto3 MediaLive client
    medialive_client = session.medialive.client()
    medialive_client: types_aiobotocore_medialive.client.MediaLiveClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_medialive.client import MediaLiveClient

from boto34.aioboto3.service_factory import ServiceFactory


class MediaLiveService(ServiceFactory[MediaLiveClient]):
    SERVICE_NAME = "medialive"
    _SERVICE_PROP = "medialive"
