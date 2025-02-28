"""
Wrapper for aiobotocore KinesisAnalytics service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisanalytics/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_kinesisanalytics.client import KinesisAnalyticsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class KinesisAnalyticsService(ServiceFactory[KinesisAnalyticsClient]):
    """
    KinesisAnalytics service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisanalytics/)
    """
