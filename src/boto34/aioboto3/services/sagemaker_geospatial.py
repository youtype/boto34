"""
Wrapper for aioboto3 SageMakergeospatialcapabilities service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sagemaker_geospatial/)

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
    # Returns type annotated aioboto3 SageMakergeospatialcapabilities client
    sagemaker_geospatial_client = session.sagemaker_geospatial.client()
    sagemaker_geospatial_client: (
        types_aiobotocore_sagemaker_geospatial.client.SageMakergeospatialcapabilitiesClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_sagemaker_geospatial.client import SageMakergeospatialcapabilitiesClient
except ImportError:
    SageMakergeospatialcapabilitiesClient = object  # type: ignore[misc,assignment]


class SageMakergeospatialcapabilitiesService(
    ServiceFactory[SageMakergeospatialcapabilitiesClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sagemaker-geospatial"
    _SERVICE_PROP = "sagemaker_geospatial"
