"""
Wrapper for aioboto3 RoboMaker service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_robomaker/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_robomaker.client import RoboMakerClient

from boto34.aioboto3.service_factory import ServiceFactory


class RoboMakerService(ServiceFactory[RoboMakerClient]):
    """
    RoboMaker service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_robomaker/)
    """
