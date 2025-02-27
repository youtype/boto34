"""
Wrapper for boto3 HealthImaging service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_medical_imaging/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 HealthImaging client
    medical_imaging_client = session.medical_imaging.client()
    medical_imaging_client: types_boto3_medical_imaging.client.HealthImagingClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_medical_imaging.client import HealthImagingClient
except ImportError:
    HealthImagingClient = object  # type: ignore[misc,assignment]


class HealthImagingService(
    ServiceFactory[HealthImagingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "medical-imaging"
    _SERVICE_PROP = "medical_imaging"
