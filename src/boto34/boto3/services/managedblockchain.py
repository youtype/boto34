"""
Wrapper for boto3 ManagedBlockchain service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_managedblockchain/)

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
    # Returns type annotated boto3 ManagedBlockchain client
    managedblockchain_client = session.managedblockchain.client()
    managedblockchain_client: types_boto3_managedblockchain.client.ManagedBlockchainClient
    ```
"""

from __future__ import annotations

from types_boto3_managedblockchain.client import ManagedBlockchainClient

from boto34.boto3.service_factory import ServiceFactory


class ManagedBlockchainService(ServiceFactory[ManagedBlockchainClient]):
    SERVICE_NAME = "managedblockchain"
    _SERVICE_PROP = "managedblockchain"
