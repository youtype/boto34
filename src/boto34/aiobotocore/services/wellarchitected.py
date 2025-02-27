"""
Wrapper for aiobotocore WellArchitected service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_wellarchitected/)

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
    # Returns type annotated aiobotocore WellArchitected client
    async with session.wellarchitected.create_client() as wellarchitected_client:
        wellarchitected_client: types_aiobotocore_wellarchitected.client.WellArchitectedClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_wellarchitected.client import WellArchitectedClient

from boto34.aiobotocore.service_factory import ServiceFactory


class WellArchitectedService(ServiceFactory[WellArchitectedClient]):
    SERVICE_NAME = "wellarchitected"
    _SERVICE_PROP = "wellarchitected"
