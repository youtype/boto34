"""
Wrapper for aiobotocore HealthImaging service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_medical_imaging.client import HealthImagingClient

from boto34.aiobotocore.service_factory import ServiceFactory


class HealthImagingService(ServiceFactory[HealthImagingClient]):
    """
    HealthImaging service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/)
    """
