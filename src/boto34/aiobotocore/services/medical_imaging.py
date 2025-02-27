"""
Wrapper for aiobotocore HealthImaging service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/)

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
    # Returns type annotated aiobotocore HealthImaging client
    async with session.medical_imaging.create_client() as medical_imaging_client:
        medical_imaging_client: types_aiobotocore_medical_imaging.client.HealthImagingClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_medical_imaging.client import HealthImagingClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_medical_imaging.client import HealthImagingClient
except ImportError:
    HealthImagingClient = object  # type: ignore[misc,assignment]


class HealthImagingService(
    ServiceFactory[HealthImagingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "medical-imaging"
    _SERVICE_PROP = "medical_imaging"
