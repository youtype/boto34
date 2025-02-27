"""
Wrapper for boto3 SavingsPlans service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_savingsplans/)

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
    # Returns type annotated boto3 SavingsPlans client
    savingsplans_client = session.savingsplans.client()
    savingsplans_client: types_boto3_savingsplans.client.SavingsPlansClient
    ```
"""

from __future__ import annotations

from types_boto3_savingsplans.client import SavingsPlansClient

from boto34.boto3.service_factory import ServiceFactory


class SavingsPlansService(ServiceFactory[SavingsPlansClient]):
    SERVICE_NAME = "savingsplans"
    _SERVICE_PROP = "savingsplans"
