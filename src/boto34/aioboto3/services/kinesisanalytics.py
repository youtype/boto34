"""
Wrapper for aioboto3 KinesisAnalytics service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kinesisanalytics/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 KinesisAnalytics client
    kinesisanalytics_client = session.kinesisanalytics.client()
    kinesisanalytics_client: types_aiobotocore_kinesisanalytics.client.KinesisAnalyticsClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_kinesisanalytics.client import KinesisAnalyticsClient
except ImportError:
    KinesisAnalyticsClient = object  # type: ignore[misc,assignment]


class KinesisAnalyticsService(
    ServiceFactory[KinesisAnalyticsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kinesisanalytics"
    _SERVICE_PROP = "kinesisanalytics"
