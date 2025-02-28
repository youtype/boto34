"""
Wrapper for boto3 RoboMaker service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_robomaker/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_robomaker.client import RoboMakerClient

from boto34.boto3.service_factory import ServiceFactory


class RoboMakerService(ServiceFactory[RoboMakerClient]):
    """
    RoboMaker service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_robomaker/)
    """
