"""
Wrapper for aiobotocore LocationServiceMapsV2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_geo_maps/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_geo_maps.client import LocationServiceMapsV2Client

from boto34.aiobotocore.service_factory import ServiceFactory


class LocationServiceMapsV2Service(ServiceFactory[LocationServiceMapsV2Client]):
    """
    LocationServiceMapsV2 service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_geo_maps/)
    """
