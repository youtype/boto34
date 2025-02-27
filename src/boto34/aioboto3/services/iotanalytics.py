"""
Wrapper for aioboto3 IoTAnalytics service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iotanalytics/)

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
    # Returns type annotated aioboto3 IoTAnalytics client
    iotanalytics_client = session.iotanalytics.client()
    iotanalytics_client: types_aiobotocore_iotanalytics.client.IoTAnalyticsClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_iotanalytics.client import IoTAnalyticsClient
except ImportError:
    IoTAnalyticsClient = object  # type: ignore[misc,assignment]


class IoTAnalyticsService(
    ServiceFactory[IoTAnalyticsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iotanalytics"
    _SERVICE_PROP = "iotanalytics"
