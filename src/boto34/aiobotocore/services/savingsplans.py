"""
Wrapper for aiobotocore SavingsPlans service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_savingsplans/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_savingsplans.client import SavingsPlansClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SavingsPlansService(ServiceFactory[SavingsPlansClient]):
    """
    SavingsPlans service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_savingsplans/)
    """
