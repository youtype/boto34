"""
Wrapper for boto3 KinesisAnalytics service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesisanalytics/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 KinesisAnalytics client
    kinesisanalytics_client = session.kinesisanalytics.client()
    kinesisanalytics_client: types_boto3_kinesisanalytics.client.KinesisAnalyticsClient
    ```
"""

from __future__ import annotations

from types_boto3_kinesisanalytics.client import KinesisAnalyticsClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_kinesisanalytics.client import KinesisAnalyticsClient
except ImportError:
    KinesisAnalyticsClient = object  # type: ignore[misc,assignment]


class KinesisAnalyticsService(
    ServiceFactory[KinesisAnalyticsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kinesisanalytics"
    _SERVICE_PROP = "kinesisanalytics"
