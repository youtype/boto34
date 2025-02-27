"""
Wrapper for boto3 SageMakergeospatialcapabilities service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sagemaker_geospatial/)

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
    # Returns type annotated boto3 SageMakergeospatialcapabilities client
    sagemaker_geospatial_client = session.sagemaker_geospatial.client()
    sagemaker_geospatial_client: (
        types_boto3_sagemaker_geospatial.client.SageMakergeospatialcapabilitiesClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_sagemaker_geospatial.client import SageMakergeospatialcapabilitiesClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_sagemaker_geospatial.client import SageMakergeospatialcapabilitiesClient
except ImportError:
    SageMakergeospatialcapabilitiesClient = object  # type: ignore[misc,assignment]


class SageMakergeospatialcapabilitiesService(
    ServiceFactory[SageMakergeospatialcapabilitiesClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sagemaker-geospatial"
    _SERVICE_PROP = "sagemaker_geospatial"
