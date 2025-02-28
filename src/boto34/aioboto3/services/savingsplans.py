"""
Wrapper for aioboto3 SavingsPlans service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_savingsplans/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_savingsplans.client import SavingsPlansClient

from boto34.aioboto3.service_factory import ServiceFactory


class SavingsPlansService(ServiceFactory[SavingsPlansClient]):
    """
    SavingsPlans service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_savingsplans/)
    """
