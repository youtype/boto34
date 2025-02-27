"""
Wrapper for aiobotocore SupplyChain service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_supplychain/)

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
    # Returns type annotated aiobotocore SupplyChain client
    async with session.supplychain.create_client() as supplychain_client:
        supplychain_client: types_aiobotocore_supplychain.client.SupplyChainClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_supplychain.client import SupplyChainClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SupplyChainService(ServiceFactory[SupplyChainClient]):
    SERVICE_NAME = "supplychain"
    _SERVICE_PROP = "supplychain"
