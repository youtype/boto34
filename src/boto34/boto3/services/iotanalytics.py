"""
Wrapper for boto3 IoTAnalytics service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotanalytics/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_iotanalytics.client import IoTAnalyticsClient

from boto34.boto3.service_factory import ServiceFactory


class IoTAnalyticsService(ServiceFactory[IoTAnalyticsClient]):
    """
    IoTAnalytics service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotanalytics/)
    """
