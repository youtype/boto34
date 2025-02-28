"""
Wrapper for aiobotocore ForecastService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_forecast.client import ForecastServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ForecastServiceService(ServiceFactory[ForecastServiceClient]):
    """
    ForecastService service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/)
    """
