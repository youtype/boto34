"""
Wrapper for aiobotocore SageMakergeospatialcapabilities service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_geospatial/)

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
    # Returns type annotated aiobotocore SageMakergeospatialcapabilities client
    async with session.sagemaker_geospatial.create_client() as sagemaker_geospatial_client:
        sagemaker_geospatial_client: (
            types_aiobotocore_sagemaker_geospatial.client.SageMakergeospatialcapabilitiesClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_sagemaker_geospatial.client import SageMakergeospatialcapabilitiesClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_sagemaker_geospatial.client import SageMakergeospatialcapabilitiesClient
except ImportError:
    SageMakergeospatialcapabilitiesClient = object  # type: ignore[misc,assignment]


class SageMakergeospatialcapabilitiesService(
    ServiceFactory[SageMakergeospatialcapabilitiesClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sagemaker-geospatial"
    _SERVICE_PROP = "sagemaker_geospatial"
