"""
Wrapper for aioboto3 LocationServicePlacesV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_geo_places/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_geo_places.client import LocationServicePlacesV2Client

from boto34.aioboto3.service_factory import ServiceFactory


class LocationServicePlacesV2Service(ServiceFactory[LocationServicePlacesV2Client]):
    """
    LocationServicePlacesV2 service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_geo_places/)
    """
