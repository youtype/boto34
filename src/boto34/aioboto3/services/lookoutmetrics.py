"""
Wrapper for aioboto3 LookoutMetrics service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lookoutmetrics/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_lookoutmetrics.client import LookoutMetricsClient

from boto34.aioboto3.service_factory import ServiceFactory


class LookoutMetricsService(ServiceFactory[LookoutMetricsClient]):
    """
    LookoutMetrics service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lookoutmetrics/)
    """
