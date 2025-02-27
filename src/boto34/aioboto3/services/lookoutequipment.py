"""
Wrapper for aioboto3 LookoutEquipment service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lookoutequipment/)

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
    # Returns type annotated aioboto3 LookoutEquipment client
    lookoutequipment_client = session.lookoutequipment.client()
    lookoutequipment_client: types_aiobotocore_lookoutequipment.client.LookoutEquipmentClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_lookoutequipment.client import LookoutEquipmentClient
except ImportError:
    LookoutEquipmentClient = object  # type: ignore[misc,assignment]


class LookoutEquipmentService(
    ServiceFactory[LookoutEquipmentClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "lookoutequipment"
    _SERVICE_PROP = "lookoutequipment"
