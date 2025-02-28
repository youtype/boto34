"""
Wrapper for boto3 HealthImaging service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_medical_imaging/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_medical_imaging.client import HealthImagingClient

from boto34.boto3.service_factory import ServiceFactory


class HealthImagingService(ServiceFactory[HealthImagingClient]):
    """
    HealthImaging service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_medical_imaging/)
    """
