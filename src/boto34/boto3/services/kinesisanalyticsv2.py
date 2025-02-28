"""
Wrapper for boto3 KinesisAnalyticsV2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesisanalyticsv2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_kinesisanalyticsv2.client import KinesisAnalyticsV2Client

from boto34.boto3.service_factory import ServiceFactory


class KinesisAnalyticsV2Service(ServiceFactory[KinesisAnalyticsV2Client]):
    """
    KinesisAnalyticsV2 service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesisanalyticsv2/)
    """
