"""
Wrapper for boto3 GameLift service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_gamelift/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_gamelift.client import GameLiftClient

from boto34.boto3.service_factory import ServiceFactory


class GameLiftService(ServiceFactory[GameLiftClient]):
    """
    GameLift service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_gamelift/)
    """
