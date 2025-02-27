"""
Wrapper for aiobotocore Account service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/)

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
    # Returns type annotated aiobotocore Account client
    async with session.account.create_client() as account_client:
        account_client: types_aiobotocore_account.client.AccountClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_account.client import AccountClient
except ImportError:
    AccountClient = object  # type: ignore[misc,assignment]


class AccountService(
    ServiceFactory[AccountClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "account"
    _SERVICE_PROP = "account"
