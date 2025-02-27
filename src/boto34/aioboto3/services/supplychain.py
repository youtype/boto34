"""
Wrapper for aioboto3 SupplyChain service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_supplychain/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 SupplyChain client
    supplychain_client = session.supplychain.client()
    supplychain_client: types_aiobotocore_supplychain.client.SupplyChainClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_supplychain.client import SupplyChainClient

from boto34.aioboto3.service_factory import ServiceFactory


class SupplyChainService(ServiceFactory[SupplyChainClient]):
    SERVICE_NAME = "supplychain"
    _SERVICE_PROP = "supplychain"
