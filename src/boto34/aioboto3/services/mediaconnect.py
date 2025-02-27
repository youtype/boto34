"""
Wrapper for aioboto3 MediaConnect service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mediaconnect/)

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
    # Returns type annotated aioboto3 MediaConnect client
    mediaconnect_client = session.mediaconnect.client()
    mediaconnect_client: types_aiobotocore_mediaconnect.client.MediaConnectClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_mediaconnect.client import MediaConnectClient

from boto34.aioboto3.service_factory import ServiceFactory


class MediaConnectService(ServiceFactory[MediaConnectClient]):
    SERVICE_NAME = "mediaconnect"
    _SERVICE_PROP = "mediaconnect"
