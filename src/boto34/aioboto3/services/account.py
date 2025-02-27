"""
Wrapper for aioboto3 Account service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_account/)

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
    # Returns type annotated aioboto3 Account client
    account_client = session.account.client()
    account_client: types_aiobotocore_account.client.AccountClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_account.client import AccountClient

from boto34.aioboto3.service_factory import ServiceFactory


class AccountService(ServiceFactory[AccountClient]):
    SERVICE_NAME = "account"
    _SERVICE_PROP = "account"
