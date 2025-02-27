"""
Wrapper for aiobotocore LookoutEquipment service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/)

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
    # Returns type annotated aiobotocore LookoutEquipment client
    async with session.lookoutequipment.create_client() as lookoutequipment_client:
        lookoutequipment_client: types_aiobotocore_lookoutequipment.client.LookoutEquipmentClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_lookoutequipment.client import LookoutEquipmentClient
except ImportError:
    LookoutEquipmentClient = object  # type: ignore[misc,assignment]


class LookoutEquipmentService(
    ServiceFactory[LookoutEquipmentClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "lookoutequipment"
    _SERVICE_PROP = "lookoutequipment"
