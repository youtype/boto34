"""
Wrapper for boto3 LookoutEquipment service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lookoutequipment/)

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
    # Returns type annotated boto3 LookoutEquipment client
    lookoutequipment_client = session.lookoutequipment.client()
    lookoutequipment_client: types_boto3_lookoutequipment.client.LookoutEquipmentClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_lookoutequipment.client import LookoutEquipmentClient
except ImportError:
    LookoutEquipmentClient = object  # type: ignore[misc,assignment]


class LookoutEquipmentService(
    ServiceFactory[LookoutEquipmentClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "lookoutequipment"
    _SERVICE_PROP = "lookoutequipment"
