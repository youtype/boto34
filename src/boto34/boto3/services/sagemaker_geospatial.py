"""
Wrapper for boto3 SageMakergeospatialcapabilities service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sagemaker_geospatial/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_sagemaker_geospatial.client import SageMakergeospatialcapabilitiesClient

from boto34.boto3.service_factory import ServiceFactory


class SageMakergeospatialcapabilitiesService(ServiceFactory[SageMakergeospatialcapabilitiesClient]):
    """
    SageMakergeospatialcapabilities service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sagemaker_geospatial/)
    """
