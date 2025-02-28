"""
Wrapper for boto3 ARCZonalShift service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_arc_zonal_shift/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_arc_zonal_shift.client import ARCZonalShiftClient

from boto34.boto3.service_factory import ServiceFactory


class ARCZonalShiftService(ServiceFactory[ARCZonalShiftClient]):
    """
    ARCZonalShift service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_arc_zonal_shift/)
    """
