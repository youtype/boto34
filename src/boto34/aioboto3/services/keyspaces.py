"""
Wrapper for aioboto3 Keyspaces service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_keyspaces/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_keyspaces.client import KeyspacesClient

from boto34.aioboto3.service_factory import ServiceFactory


class KeyspacesService(ServiceFactory[KeyspacesClient]):
    """
    Keyspaces service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_keyspaces/)
    """
