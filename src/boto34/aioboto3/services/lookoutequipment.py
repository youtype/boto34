"""
Wrapper for aioboto3 LookoutEquipment service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lookoutequipment/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_lookoutequipment.client import LookoutEquipmentClient

from boto34.aioboto3.service_factory import ServiceFactory


class LookoutEquipmentService(ServiceFactory[LookoutEquipmentClient]):
    """
    LookoutEquipment service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lookoutequipment/)
    """
