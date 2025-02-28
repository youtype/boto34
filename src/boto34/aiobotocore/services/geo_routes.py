"""
Wrapper for aiobotocore LocationServiceRoutesV2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_geo_routes/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_geo_routes.client import LocationServiceRoutesV2Client

from boto34.aiobotocore.service_factory import ServiceFactory


class LocationServiceRoutesV2Service(ServiceFactory[LocationServiceRoutesV2Client]):
    """
    LocationServiceRoutesV2 service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_geo_routes/)
    """
