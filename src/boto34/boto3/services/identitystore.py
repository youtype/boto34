"""
Wrapper for boto3 IdentityStore service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_identitystore/)

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
    # Returns type annotated boto3 IdentityStore client
    identitystore_client = session.identitystore.client()
    identitystore_client: types_boto3_identitystore.client.IdentityStoreClient
    ```
"""

from __future__ import annotations

from types_boto3_identitystore.client import IdentityStoreClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_identitystore.client import IdentityStoreClient
except ImportError:
    IdentityStoreClient = object  # type: ignore[misc,assignment]


class IdentityStoreService(
    ServiceFactory[IdentityStoreClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "identitystore"
    _SERVICE_PROP = "identitystore"
