"""
Wrapper for aiobotocore Keyspaces service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_keyspaces/)

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
    # Returns type annotated aiobotocore Keyspaces client
    async with session.keyspaces.create_client() as keyspaces_client:
        keyspaces_client: types_aiobotocore_keyspaces.client.KeyspacesClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_keyspaces.client import KeyspacesClient

from boto34.aiobotocore.service_factory import ServiceFactory


class KeyspacesService(ServiceFactory[KeyspacesClient]):
    SERVICE_NAME = "keyspaces"
    _SERVICE_PROP = "keyspaces"
