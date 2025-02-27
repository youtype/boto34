"""
Wrapper for aioboto3 MediaTailor service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mediatailor/)

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
    # Returns type annotated aioboto3 MediaTailor client
    mediatailor_client = session.mediatailor.client()
    mediatailor_client: types_aiobotocore_mediatailor.client.MediaTailorClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_mediatailor.client import MediaTailorClient

from boto34.aioboto3.service_factory import ServiceFactory


class MediaTailorService(ServiceFactory[MediaTailorClient]):
    SERVICE_NAME = "mediatailor"
    _SERVICE_PROP = "mediatailor"
