"""
Wrapper for aiobotocore Keyspaces service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_keyspaces/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_keyspaces.client import KeyspacesClient

from boto34.aiobotocore.service_factory import ServiceFactory


class KeyspacesService(ServiceFactory[KeyspacesClient]):
    """
    Keyspaces service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_keyspaces/)
    """
