"""
Wrapper for aiobotocore Budgets service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_budgets/)

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
    # Returns type annotated aiobotocore Budgets client
    async with session.budgets.create_client() as budgets_client:
        budgets_client: types_aiobotocore_budgets.client.BudgetsClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_budgets.client import BudgetsClient
except ImportError:
    BudgetsClient = object  # type: ignore[misc,assignment]


class BudgetsService(
    ServiceFactory[BudgetsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "budgets"
    _SERVICE_PROP = "budgets"
