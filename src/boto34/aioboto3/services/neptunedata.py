"""
Wrapper for aioboto3 NeptuneData service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_neptunedata/)

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
    # Returns type annotated aioboto3 NeptuneData client
    neptunedata_client = session.neptunedata.client()
    neptunedata_client: types_aiobotocore_neptunedata.client.NeptuneDataClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_neptunedata.client import NeptuneDataClient
except ImportError:
    NeptuneDataClient = object  # type: ignore[misc,assignment]


class NeptuneDataService(
    ServiceFactory[NeptuneDataClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "neptunedata"
    _SERVICE_PROP = "neptunedata"
