"""
Wrapper for aiobotocore Imagebuilder service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_imagebuilder/)

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
    # Returns type annotated aiobotocore Imagebuilder client
    async with session.imagebuilder.create_client() as imagebuilder_client:
        imagebuilder_client: types_aiobotocore_imagebuilder.client.ImagebuilderClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_imagebuilder.client import ImagebuilderClient
except ImportError:
    ImagebuilderClient = object  # type: ignore[misc,assignment]


class ImagebuilderService(
    ServiceFactory[ImagebuilderClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "imagebuilder"
    _SERVICE_PROP = "imagebuilder"
