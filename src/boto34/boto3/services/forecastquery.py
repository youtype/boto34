"""
Wrapper for boto3 ForecastQueryService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_forecastquery/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_forecastquery.client import ForecastQueryServiceClient

from boto34.boto3.service_factory import ServiceFactory


class ForecastQueryServiceService(ServiceFactory[ForecastQueryServiceClient]):
    """
    ForecastQueryService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_forecastquery/)
    """
