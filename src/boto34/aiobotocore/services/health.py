"""
Wrapper for aiobotocore Health service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_health/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_health.client import HealthClient

from boto34.aiobotocore.service_factory import ServiceFactory


class HealthService(ServiceFactory[HealthClient]):
    """
    Health service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_health/)
    """
