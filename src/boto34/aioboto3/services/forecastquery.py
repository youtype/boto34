"""
Wrapper for aioboto3 ForecastQueryService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_forecastquery/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_forecastquery.client import ForecastQueryServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class ForecastQueryServiceService(ServiceFactory[ForecastQueryServiceClient]):
    """
    ForecastQueryService service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_forecastquery/)
    """
