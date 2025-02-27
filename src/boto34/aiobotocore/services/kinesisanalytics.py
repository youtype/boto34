"""
Wrapper for aiobotocore KinesisAnalytics service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisanalytics/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore KinesisAnalytics client
    async with session.kinesisanalytics.create_client() as kinesisanalytics_client:
        kinesisanalytics_client: types_aiobotocore_kinesisanalytics.client.KinesisAnalyticsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_kinesisanalytics.client import KinesisAnalyticsClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_kinesisanalytics.client import KinesisAnalyticsClient
except ImportError:
    KinesisAnalyticsClient = object  # type: ignore[misc,assignment]


class KinesisAnalyticsService(
    ServiceFactory[KinesisAnalyticsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kinesisanalytics"
    _SERVICE_PROP = "kinesisanalytics"
