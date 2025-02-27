"""
Wrapper for boto3 Account service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_account/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 Account client
    account_client = session.account.client()
    account_client: types_boto3_account.client.AccountClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_account.client import AccountClient
except ImportError:
    AccountClient = object  # type: ignore[misc,assignment]


class AccountService(
    ServiceFactory[AccountClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "account"
    _SERVICE_PROP = "account"
