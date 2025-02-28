"""
Wrapper for aioboto3 Account service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_account/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_account.client import AccountClient

from boto34.aioboto3.service_factory import ServiceFactory


class AccountService(ServiceFactory[AccountClient]):
    """
    Account service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_account/)
    """
