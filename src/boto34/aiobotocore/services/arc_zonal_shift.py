"""
Wrapper for aiobotocore ARCZonalShift service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_arc_zonal_shift/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore ARCZonalShift client
    async with session.arc_zonal_shift.create_client() as arc_zonal_shift_client:
        arc_zonal_shift_client: types_aiobotocore_arc_zonal_shift.client.ARCZonalShiftClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_arc_zonal_shift.client import ARCZonalShiftClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_arc_zonal_shift.client import ARCZonalShiftClient
except ImportError:
    ARCZonalShiftClient = object  # type: ignore[misc,assignment]


class ARCZonalShiftService(
    ServiceFactory[ARCZonalShiftClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "arc-zonal-shift"
    _SERVICE_PROP = "arc_zonal_shift"
