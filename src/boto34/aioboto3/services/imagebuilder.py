"""
Wrapper for aioboto3 Imagebuilder service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_imagebuilder/)

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
    # Returns type annotated aioboto3 Imagebuilder client
    imagebuilder_client = session.imagebuilder.client()
    imagebuilder_client: types_aiobotocore_imagebuilder.client.ImagebuilderClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_imagebuilder.client import ImagebuilderClient
except ImportError:
    ImagebuilderClient = object  # type: ignore[misc,assignment]


class ImagebuilderService(
    ServiceFactory[ImagebuilderClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "imagebuilder"
    _SERVICE_PROP = "imagebuilder"
