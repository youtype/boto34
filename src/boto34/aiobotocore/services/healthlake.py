"""
Wrapper for aiobotocore HealthLake service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_healthlake/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_healthlake.client import HealthLakeClient

from boto34.aiobotocore.service_factory import ServiceFactory


class HealthLakeService(ServiceFactory[HealthLakeClient]):
    """
    HealthLake service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_healthlake/)
    """
