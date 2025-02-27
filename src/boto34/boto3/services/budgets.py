"""
Wrapper for boto3 Budgets service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_budgets/)

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
    # Returns type annotated boto3 Budgets client
    budgets_client = session.budgets.client()
    budgets_client: types_boto3_budgets.client.BudgetsClient
    ```
"""

from __future__ import annotations

from types_boto3_budgets.client import BudgetsClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_budgets.client import BudgetsClient
except ImportError:
    BudgetsClient = object  # type: ignore[misc,assignment]


class BudgetsService(
    ServiceFactory[BudgetsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "budgets"
    _SERVICE_PROP = "budgets"
