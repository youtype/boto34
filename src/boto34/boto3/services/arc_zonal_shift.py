"""
Wrapper for boto3 ARCZonalShift service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_arc_zonal_shift/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 ARCZonalShift client
    arc_zonal_shift_client = session.arc_zonal_shift.client()
    arc_zonal_shift_client: types_boto3_arc_zonal_shift.client.ARCZonalShiftClient
    ```
"""

from __future__ import annotations

from types_boto3_arc_zonal_shift.client import ARCZonalShiftClient

from boto34.boto3.service_factory import ServiceFactory


class ARCZonalShiftService(ServiceFactory[ARCZonalShiftClient]):
    SERVICE_NAME = "arc-zonal-shift"
    _SERVICE_PROP = "arc_zonal_shift"
