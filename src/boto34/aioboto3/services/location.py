"""
Wrapper for aioboto3 LocationService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_location/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_location.client import LocationServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class LocationServiceService(ServiceFactory[LocationServiceClient]):
    """
    LocationService service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_location/)
    """
