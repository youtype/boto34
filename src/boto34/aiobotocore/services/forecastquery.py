"""
Wrapper for aiobotocore ForecastQueryService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecastquery/)

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
    # Returns type annotated aiobotocore ForecastQueryService client
    async with session.forecastquery.create_client() as forecastquery_client:
        forecastquery_client: types_aiobotocore_forecastquery.client.ForecastQueryServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_forecastquery.client import ForecastQueryServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ForecastQueryServiceService(ServiceFactory[ForecastQueryServiceClient]):
    SERVICE_NAME = "forecastquery"
    _SERVICE_PROP = "forecastquery"
