"""
Wrapper for aioboto3 ForecastService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_forecast/)

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
    # Returns type annotated aioboto3 ForecastService client
    forecast_client = session.forecast.client()
    forecast_client: types_aiobotocore_forecast.client.ForecastServiceClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_forecast.client import ForecastServiceClient
except ImportError:
    ForecastServiceClient = object  # type: ignore[misc,assignment]


class ForecastServiceService(
    ServiceFactory[ForecastServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "forecast"
    _SERVICE_PROP = "forecast"
