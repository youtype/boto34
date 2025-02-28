"""
Wrapper for boto3 Account service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_account/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_account.client import AccountClient

from boto34.boto3.service_factory import ServiceFactory


class AccountService(ServiceFactory[AccountClient]):
    """
    Account service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_account/)
    """
