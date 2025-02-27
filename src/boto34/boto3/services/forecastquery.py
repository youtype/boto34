"""
Wrapper for boto3 ForecastQueryService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_forecastquery/)

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
    # Returns type annotated boto3 ForecastQueryService client
    forecastquery_client = session.forecastquery.client()
    forecastquery_client: types_boto3_forecastquery.client.ForecastQueryServiceClient
    ```
"""

from __future__ import annotations

from types_boto3_forecastquery.client import ForecastQueryServiceClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_forecastquery.client import ForecastQueryServiceClient
except ImportError:
    ForecastQueryServiceClient = object  # type: ignore[misc,assignment]


class ForecastQueryServiceService(
    ServiceFactory[ForecastQueryServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "forecastquery"
    _SERVICE_PROP = "forecastquery"
