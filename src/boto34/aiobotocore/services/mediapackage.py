"""
Wrapper for aiobotocore MediaPackage service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediapackage/)

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
    # Returns type annotated aiobotocore MediaPackage client
    async with session.mediapackage.create_client() as mediapackage_client:
        mediapackage_client: types_aiobotocore_mediapackage.client.MediaPackageClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_mediapackage.client import MediaPackageClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MediaPackageService(ServiceFactory[MediaPackageClient]):
    SERVICE_NAME = "mediapackage"
    _SERVICE_PROP = "mediapackage"
