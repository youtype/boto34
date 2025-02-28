"""
Wrapper for boto3 KinesisAnalytics service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesisanalytics/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_kinesisanalytics.client import KinesisAnalyticsClient

from boto34.boto3.service_factory import ServiceFactory


class KinesisAnalyticsService(ServiceFactory[KinesisAnalyticsClient]):
    """
    KinesisAnalytics service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesisanalytics/)
    """
