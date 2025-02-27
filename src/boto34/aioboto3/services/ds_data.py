"""
Wrapper for aioboto3 DirectoryServiceData service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ds_data/)

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
    # Returns type annotated aioboto3 DirectoryServiceData client
    ds_data_client = session.ds_data.client()
    ds_data_client: types_aiobotocore_ds_data.client.DirectoryServiceDataClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_ds_data.client import DirectoryServiceDataClient
except ImportError:
    DirectoryServiceDataClient = object  # type: ignore[misc,assignment]


class DirectoryServiceDataService(
    ServiceFactory[DirectoryServiceDataClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ds-data"
    _SERVICE_PROP = "ds_data"
