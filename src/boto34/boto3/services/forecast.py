"""
Wrapper for boto3 ForecastService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_forecast/)

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
    # Returns type annotated boto3 ForecastService client
    forecast_client = session.forecast.client()
    forecast_client: types_boto3_forecast.client.ForecastServiceClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_forecast.client import ForecastServiceClient
except ImportError:
    ForecastServiceClient = object  # type: ignore[misc,assignment]


class ForecastServiceService(
    ServiceFactory[ForecastServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "forecast"
    _SERVICE_PROP = "forecast"
