"""
Wrapper for aioboto3 MediaPackage service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mediapackage/)

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
    # Returns type annotated aioboto3 MediaPackage client
    mediapackage_client = session.mediapackage.client()
    mediapackage_client: types_aiobotocore_mediapackage.client.MediaPackageClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_mediapackage.client import MediaPackageClient

from boto34.aioboto3.service_factory import ServiceFactory


class MediaPackageService(ServiceFactory[MediaPackageClient]):
    SERVICE_NAME = "mediapackage"
    _SERVICE_PROP = "mediapackage"
