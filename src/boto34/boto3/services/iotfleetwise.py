"""
Wrapper for boto3 IoTFleetWise service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotfleetwise/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_iotfleetwise.client import IoTFleetWiseClient

from boto34.boto3.service_factory import ServiceFactory


class IoTFleetWiseService(ServiceFactory[IoTFleetWiseClient]):
    """
    IoTFleetWise service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotfleetwise/)
    """
