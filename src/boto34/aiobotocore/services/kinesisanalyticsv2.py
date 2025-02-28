"""
Wrapper for aiobotocore KinesisAnalyticsV2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisanalyticsv2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_kinesisanalyticsv2.client import KinesisAnalyticsV2Client

from boto34.aiobotocore.service_factory import ServiceFactory


class KinesisAnalyticsV2Service(ServiceFactory[KinesisAnalyticsV2Client]):
    """
    KinesisAnalyticsV2 service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisanalyticsv2/)
    """
