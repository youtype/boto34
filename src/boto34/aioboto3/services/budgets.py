"""
Wrapper for aioboto3 Budgets service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_budgets/)

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
    # Returns type annotated aioboto3 Budgets client
    budgets_client = session.budgets.client()
    budgets_client: types_aiobotocore_budgets.client.BudgetsClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_budgets.client import BudgetsClient
except ImportError:
    BudgetsClient = object  # type: ignore[misc,assignment]


class BudgetsService(
    ServiceFactory[BudgetsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "budgets"
    _SERVICE_PROP = "budgets"
