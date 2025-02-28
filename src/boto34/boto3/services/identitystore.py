"""
Wrapper for boto3 IdentityStore service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_identitystore/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_identitystore.client import IdentityStoreClient

from boto34.boto3.service_factory import ServiceFactory


class IdentityStoreService(ServiceFactory[IdentityStoreClient]):
    """
    IdentityStore service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_identitystore/)
    """
