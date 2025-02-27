"""
Wrapper for aiobotocore Mediapackagev2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediapackagev2/)

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
    # Returns type annotated aiobotocore Mediapackagev2 client
    async with session.mediapackagev2.create_client() as mediapackagev2_client:
        mediapackagev2_client: types_aiobotocore_mediapackagev2.client.Mediapackagev2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_mediapackagev2.client import Mediapackagev2Client

from boto34.aiobotocore.service_factory import ServiceFactory


class Mediapackagev2Service(ServiceFactory[Mediapackagev2Client]):
    SERVICE_NAME = "mediapackagev2"
    _SERVICE_PROP = "mediapackagev2"
