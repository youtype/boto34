"""
Wrapper for aioboto3 SageMakergeospatialcapabilities service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sagemaker_geospatial/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sagemaker_geospatial.client import SageMakergeospatialcapabilitiesClient

from boto34.aioboto3.service_factory import ServiceFactory


class SageMakergeospatialcapabilitiesService(ServiceFactory[SageMakergeospatialcapabilitiesClient]):
    """
    SageMakergeospatialcapabilities service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sagemaker_geospatial/)
    """
