"""
Wrapper for aiobotocore ForecastService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/)

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
    # Returns type annotated aiobotocore ForecastService client
    async with session.forecast.create_client() as forecast_client:
        forecast_client: types_aiobotocore_forecast.client.ForecastServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_forecast.client import ForecastServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ForecastServiceService(ServiceFactory[ForecastServiceClient]):
    SERVICE_NAME = "forecast"
    _SERVICE_PROP = "forecast"
