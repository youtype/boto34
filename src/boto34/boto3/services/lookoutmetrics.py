"""
Wrapper for boto3 LookoutMetrics service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lookoutmetrics/)

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
    # Returns type annotated boto3 LookoutMetrics client
    lookoutmetrics_client = session.lookoutmetrics.client()
    lookoutmetrics_client: types_boto3_lookoutmetrics.client.LookoutMetricsClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_lookoutmetrics.client import LookoutMetricsClient
except ImportError:
    LookoutMetricsClient = object  # type: ignore[misc,assignment]


class LookoutMetricsService(
    ServiceFactory[LookoutMetricsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "lookoutmetrics"
    _SERVICE_PROP = "lookoutmetrics"
