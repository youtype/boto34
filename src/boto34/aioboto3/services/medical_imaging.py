"""
Wrapper for aioboto3 HealthImaging service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_medical_imaging/)

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
    # Returns type annotated aioboto3 HealthImaging client
    medical_imaging_client = session.medical_imaging.client()
    medical_imaging_client: types_aiobotocore_medical_imaging.client.HealthImagingClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_medical_imaging.client import HealthImagingClient
except ImportError:
    HealthImagingClient = object  # type: ignore[misc,assignment]


class HealthImagingService(
    ServiceFactory[HealthImagingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "medical-imaging"
    _SERVICE_PROP = "medical_imaging"
