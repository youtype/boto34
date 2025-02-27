"""
Wrapper for aioboto3 IdentityStore service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_identitystore/)

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
    # Returns type annotated aioboto3 IdentityStore client
    identitystore_client = session.identitystore.client()
    identitystore_client: types_aiobotocore_identitystore.client.IdentityStoreClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_identitystore.client import IdentityStoreClient

from boto34.aioboto3.service_factory import ServiceFactory


class IdentityStoreService(ServiceFactory[IdentityStoreClient]):
    SERVICE_NAME = "identitystore"
    _SERVICE_PROP = "identitystore"
