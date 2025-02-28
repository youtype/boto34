"""
Wrapper for boto3 IoTTwinMaker service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iottwinmaker/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_iottwinmaker.client import IoTTwinMakerClient

from boto34.boto3.service_factory import ServiceFactory


class IoTTwinMakerService(ServiceFactory[IoTTwinMakerClient]):
    """
    IoTTwinMaker service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iottwinmaker/)
    """
