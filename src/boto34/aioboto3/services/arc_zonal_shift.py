"""
Wrapper for aioboto3 ARCZonalShift service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_arc_zonal_shift/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 ARCZonalShift client
    arc_zonal_shift_client = session.arc_zonal_shift.client()
    arc_zonal_shift_client: types_aiobotocore_arc_zonal_shift.client.ARCZonalShiftClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_arc_zonal_shift.client import ARCZonalShiftClient

from boto34.aioboto3.service_factory import ServiceFactory


class ARCZonalShiftService(ServiceFactory[ARCZonalShiftClient]):
    SERVICE_NAME = "arc-zonal-shift"
    _SERVICE_PROP = "arc_zonal_shift"
