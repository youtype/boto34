"""
Wrapper for boto3 ControlTower service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_controltower/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_controltower.client import ControlTowerClient

from boto34.boto3.service_factory import ServiceFactory


class ControlTowerService(ServiceFactory[ControlTowerClient]):
    """
    ControlTower service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_controltower/)
    """
