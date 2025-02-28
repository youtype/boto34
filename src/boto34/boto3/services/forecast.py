"""
Wrapper for boto3 ForecastService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_forecast/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_forecast.client import ForecastServiceClient

from boto34.boto3.service_factory import ServiceFactory


class ForecastServiceService(ServiceFactory[ForecastServiceClient]):
    """
    ForecastService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_forecast/)
    """
