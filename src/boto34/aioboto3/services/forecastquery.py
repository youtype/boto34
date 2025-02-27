"""
Wrapper for aioboto3 ForecastQueryService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_forecastquery/)

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
    # Returns type annotated aioboto3 ForecastQueryService client
    forecastquery_client = session.forecastquery.client()
    forecastquery_client: types_aiobotocore_forecastquery.client.ForecastQueryServiceClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_forecastquery.client import ForecastQueryServiceClient
except ImportError:
    ForecastQueryServiceClient = object  # type: ignore[misc,assignment]


class ForecastQueryServiceService(
    ServiceFactory[ForecastQueryServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "forecastquery"
    _SERVICE_PROP = "forecastquery"
