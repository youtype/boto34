"""
Wrapper for aioboto3 GuardDuty service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_guardduty/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_guardduty.client import GuardDutyClient

from boto34.aioboto3.service_factory import ServiceFactory


class GuardDutyService(ServiceFactory[GuardDutyClient]):
    """
    GuardDuty service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_guardduty/)
    """
