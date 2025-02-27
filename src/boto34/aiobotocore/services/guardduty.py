"""
Wrapper for aiobotocore GuardDuty service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_guardduty/)

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
    # Returns type annotated aiobotocore GuardDuty client
    async with session.guardduty.create_client() as guardduty_client:
        guardduty_client: types_aiobotocore_guardduty.client.GuardDutyClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_guardduty.client import GuardDutyClient
except ImportError:
    GuardDutyClient = object  # type: ignore[misc,assignment]


class GuardDutyService(
    ServiceFactory[GuardDutyClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "guardduty"
    _SERVICE_PROP = "guardduty"
