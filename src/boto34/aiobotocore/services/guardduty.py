"""
Wrapper for aiobotocore GuardDuty service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_guardduty/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_guardduty.client import GuardDutyClient

from boto34.aiobotocore.service_factory import ServiceFactory


class GuardDutyService(ServiceFactory[GuardDutyClient]):
    """
    GuardDuty service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_guardduty/)
    """
