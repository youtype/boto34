"""
Wrapper for boto3 IoTAnalytics service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotanalytics/)

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
    # Returns type annotated boto3 IoTAnalytics client
    iotanalytics_client = session.iotanalytics.client()
    iotanalytics_client: types_boto3_iotanalytics.client.IoTAnalyticsClient
    ```
"""

from __future__ import annotations

from types_boto3_iotanalytics.client import IoTAnalyticsClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_iotanalytics.client import IoTAnalyticsClient
except ImportError:
    IoTAnalyticsClient = object  # type: ignore[misc,assignment]


class IoTAnalyticsService(
    ServiceFactory[IoTAnalyticsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iotanalytics"
    _SERVICE_PROP = "iotanalytics"
