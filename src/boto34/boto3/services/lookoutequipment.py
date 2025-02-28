"""
Wrapper for boto3 LookoutEquipment service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lookoutequipment/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_lookoutequipment.client import LookoutEquipmentClient

from boto34.boto3.service_factory import ServiceFactory


class LookoutEquipmentService(ServiceFactory[LookoutEquipmentClient]):
    """
    LookoutEquipment service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lookoutequipment/)
    """
