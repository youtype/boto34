"""
Wrapper for aiobotocore ControlTower service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_controltower/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_controltower.client import ControlTowerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ControlTowerService(ServiceFactory[ControlTowerClient]):
    """
    ControlTower service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_controltower/)
    """
