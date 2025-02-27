"""
Wrapper for boto3 NeptuneData service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_neptunedata/)

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
    # Returns type annotated boto3 NeptuneData client
    neptunedata_client = session.neptunedata.client()
    neptunedata_client: types_boto3_neptunedata.client.NeptuneDataClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_neptunedata.client import NeptuneDataClient
except ImportError:
    NeptuneDataClient = object  # type: ignore[misc,assignment]


class NeptuneDataService(
    ServiceFactory[NeptuneDataClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "neptunedata"
    _SERVICE_PROP = "neptunedata"
