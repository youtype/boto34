"""
Wrapper for aioboto3 DataExchange service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_dataexchange/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_dataexchange.client import DataExchangeClient

from boto34.aioboto3.service_factory import ServiceFactory


class DataExchangeService(ServiceFactory[DataExchangeClient]):
    """
    DataExchange service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_dataexchange/)
    """
