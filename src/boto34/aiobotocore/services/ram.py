"""
Wrapper for aiobotocore RAM service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ram/)

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
    # Returns type annotated aiobotocore RAM client
    async with session.ram.create_client() as ram_client:
        ram_client: types_aiobotocore_ram.client.RAMClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_ram.client import RAMClient

from boto34.aiobotocore.service_factory import ServiceFactory


class RAMService(ServiceFactory[RAMClient]):
    SERVICE_NAME = "ram"
    _SERVICE_PROP = "ram"
