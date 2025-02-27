"""
Wrapper for aioboto3 Rekognition service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_rekognition/)

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
    # Returns type annotated aioboto3 Rekognition client
    rekognition_client = session.rekognition.client()
    rekognition_client: types_aiobotocore_rekognition.client.RekognitionClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_rekognition.client import RekognitionClient
except ImportError:
    RekognitionClient = object  # type: ignore[misc,assignment]


class RekognitionService(
    ServiceFactory[RekognitionClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "rekognition"
    _SERVICE_PROP = "rekognition"
