"""
Wrapper for aioboto3 DataExchange service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_dataexchange/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 DataExchange client
    dataexchange_client = session.dataexchange.client()
    dataexchange_client: types_aiobotocore_dataexchange.client.DataExchangeClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_dataexchange.client import DataExchangeClient

from boto34.aioboto3.service_factory import ServiceFactory


class DataExchangeService(ServiceFactory[DataExchangeClient]):
    SERVICE_NAME = "dataexchange"
    _SERVICE_PROP = "dataexchange"
