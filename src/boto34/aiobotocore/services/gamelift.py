"""
Wrapper for aiobotocore GameLift service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_gamelift/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_gamelift.client import GameLiftClient

from boto34.aiobotocore.service_factory import ServiceFactory


class GameLiftService(ServiceFactory[GameLiftClient]):
    """
    GameLift service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_gamelift/)
    """
