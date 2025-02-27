"""
Wrapper for aiobotocore ControlTower service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_controltower/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore ControlTower client
    async with session.controltower.create_client() as controltower_client:
        controltower_client: types_aiobotocore_controltower.client.ControlTowerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_controltower.client import ControlTowerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ControlTowerService(ServiceFactory[ControlTowerClient]):
    SERVICE_NAME = "controltower"
    _SERVICE_PROP = "controltower"
