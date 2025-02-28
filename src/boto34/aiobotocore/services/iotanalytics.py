"""
Wrapper for aiobotocore IoTAnalytics service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotanalytics/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_iotanalytics.client import IoTAnalyticsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class IoTAnalyticsService(ServiceFactory[IoTAnalyticsClient]):
    """
    IoTAnalytics service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotanalytics/)
    """
