"""
Wrapper for boto3 SupplyChain service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_supplychain/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 SupplyChain client
    supplychain_client = session.supplychain.client()
    supplychain_client: types_boto3_supplychain.client.SupplyChainClient
    ```
"""

from __future__ import annotations

from types_boto3_supplychain.client import SupplyChainClient

from boto34.boto3.service_factory import ServiceFactory


class SupplyChainService(ServiceFactory[SupplyChainClient]):
    SERVICE_NAME = "supplychain"
    _SERVICE_PROP = "supplychain"
