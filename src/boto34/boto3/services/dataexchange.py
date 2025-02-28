"""
Wrapper for boto3 DataExchange service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_dataexchange/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_dataexchange.client import DataExchangeClient

from boto34.boto3.service_factory import ServiceFactory


class DataExchangeService(ServiceFactory[DataExchangeClient]):
    """
    DataExchange service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_dataexchange/)
    """
