"""
Wrapper for aiobotocore AppFabric service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/)

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
    # Returns type annotated aiobotocore AppFabric client
    async with session.appfabric.create_client() as appfabric_client:
        appfabric_client: types_aiobotocore_appfabric.client.AppFabricClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_appfabric.client import AppFabricClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AppFabricService(ServiceFactory[AppFabricClient]):
    SERVICE_NAME = "appfabric"
    _SERVICE_PROP = "appfabric"
