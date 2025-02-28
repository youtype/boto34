"""
Wrapper for aiobotocore Budgets service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_budgets/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_budgets.client import BudgetsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class BudgetsService(ServiceFactory[BudgetsClient]):
    """
    Budgets service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_budgets/)
    """
