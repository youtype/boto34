"""
Wrapper for aiobotocore SavingsPlans service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_savingsplans/)

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
    # Returns type annotated aiobotocore SavingsPlans client
    async with session.savingsplans.create_client() as savingsplans_client:
        savingsplans_client: types_aiobotocore_savingsplans.client.SavingsPlansClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_savingsplans.client import SavingsPlansClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_savingsplans.client import SavingsPlansClient
except ImportError:
    SavingsPlansClient = object  # type: ignore[misc,assignment]


class SavingsPlansService(
    ServiceFactory[SavingsPlansClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "savingsplans"
    _SERVICE_PROP = "savingsplans"
