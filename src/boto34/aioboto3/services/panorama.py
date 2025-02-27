"""
Wrapper for aioboto3 Panorama service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_panorama/)

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
    # Returns type annotated aioboto3 Panorama client
    panorama_client = session.panorama.client()
    panorama_client: types_aiobotocore_panorama.client.PanoramaClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_panorama.client import PanoramaClient

from boto34.aioboto3.service_factory import ServiceFactory


class PanoramaService(ServiceFactory[PanoramaClient]):
    SERVICE_NAME = "panorama"
    _SERVICE_PROP = "panorama"
