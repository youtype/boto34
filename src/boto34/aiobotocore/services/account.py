"""
Wrapper for aiobotocore Account service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_account.client import AccountClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AccountService(ServiceFactory[AccountClient]):
    """
    Account service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/)
    """
