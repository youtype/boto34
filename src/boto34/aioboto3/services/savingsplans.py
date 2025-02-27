"""
Wrapper for aioboto3 SavingsPlans service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_savingsplans/)

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
    # Returns type annotated aioboto3 SavingsPlans client
    savingsplans_client = session.savingsplans.client()
    savingsplans_client: types_aiobotocore_savingsplans.client.SavingsPlansClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_savingsplans.client import SavingsPlansClient

from boto34.aioboto3.service_factory import ServiceFactory


class SavingsPlansService(ServiceFactory[SavingsPlansClient]):
    SERVICE_NAME = "savingsplans"
    _SERVICE_PROP = "savingsplans"
