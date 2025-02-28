"""
Wrapper for aiobotocore ForecastQueryService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecastquery/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_forecastquery.client import ForecastQueryServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ForecastQueryServiceService(ServiceFactory[ForecastQueryServiceClient]):
    """
    ForecastQueryService service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecastquery/)
    """
