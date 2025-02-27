"""
Wrapper for boto3 DataExchange service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_dataexchange/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 DataExchange client
    dataexchange_client = session.dataexchange.client()
    dataexchange_client: types_boto3_dataexchange.client.DataExchangeClient
    ```
"""

from __future__ import annotations

from types_boto3_dataexchange.client import DataExchangeClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_dataexchange.client import DataExchangeClient
except ImportError:
    DataExchangeClient = object  # type: ignore[misc,assignment]


class DataExchangeService(
    ServiceFactory[DataExchangeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "dataexchange"
    _SERVICE_PROP = "dataexchange"
