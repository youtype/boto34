"""
Wrapper for aiobotocore Panorama service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_panorama/)

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
    # Returns type annotated aiobotocore Panorama client
    async with session.panorama.create_client() as panorama_client:
        panorama_client: types_aiobotocore_panorama.client.PanoramaClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_panorama.client import PanoramaClient

from boto34.aiobotocore.service_factory import ServiceFactory


class PanoramaService(ServiceFactory[PanoramaClient]):
    SERVICE_NAME = "panorama"
    _SERVICE_PROP = "panorama"
