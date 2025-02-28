"""
Wrapper for aioboto3 IdentityStore service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_identitystore/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_identitystore.client import IdentityStoreClient

from boto34.aioboto3.service_factory import ServiceFactory


class IdentityStoreService(ServiceFactory[IdentityStoreClient]):
    """
    IdentityStore service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_identitystore/)
    """
