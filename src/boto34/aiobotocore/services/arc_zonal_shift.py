"""
Wrapper for aiobotocore ARCZonalShift service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_arc_zonal_shift/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_arc_zonal_shift.client import ARCZonalShiftClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ARCZonalShiftService(ServiceFactory[ARCZonalShiftClient]):
    """
    ARCZonalShift service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_arc_zonal_shift/)
    """
