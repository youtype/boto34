"""
Wrapper for aioboto3 GuardDuty service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_guardduty/)

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
    # Returns type annotated aioboto3 GuardDuty client
    guardduty_client = session.guardduty.client()
    guardduty_client: types_aiobotocore_guardduty.client.GuardDutyClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_guardduty.client import GuardDutyClient
except ImportError:
    GuardDutyClient = object  # type: ignore[misc,assignment]


class GuardDutyService(
    ServiceFactory[GuardDutyClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "guardduty"
    _SERVICE_PROP = "guardduty"
