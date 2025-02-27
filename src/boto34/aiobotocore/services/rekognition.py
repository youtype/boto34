"""
Wrapper for aiobotocore Rekognition service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/)

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
    # Returns type annotated aiobotocore Rekognition client
    async with session.rekognition.create_client() as rekognition_client:
        rekognition_client: types_aiobotocore_rekognition.client.RekognitionClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_rekognition.client import RekognitionClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_rekognition.client import RekognitionClient
except ImportError:
    RekognitionClient = object  # type: ignore[misc,assignment]


class RekognitionService(
    ServiceFactory[RekognitionClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "rekognition"
    _SERVICE_PROP = "rekognition"
