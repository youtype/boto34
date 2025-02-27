"""
Wrapper for aioboto3 Keyspaces service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_keyspaces/)

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
    # Returns type annotated aioboto3 Keyspaces client
    keyspaces_client = session.keyspaces.client()
    keyspaces_client: types_aiobotocore_keyspaces.client.KeyspacesClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_keyspaces.client import KeyspacesClient

from boto34.aioboto3.service_factory import ServiceFactory


class KeyspacesService(ServiceFactory[KeyspacesClient]):
    SERVICE_NAME = "keyspaces"
    _SERVICE_PROP = "keyspaces"
