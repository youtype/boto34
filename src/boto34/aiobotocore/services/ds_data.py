"""
Wrapper for aiobotocore DirectoryServiceData service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ds_data/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore DirectoryServiceData client
    async with session.ds_data.create_client() as ds_data_client:
        ds_data_client: types_aiobotocore_ds_data.client.DirectoryServiceDataClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_ds_data.client import DirectoryServiceDataClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DirectoryServiceDataService(ServiceFactory[DirectoryServiceDataClient]):
    SERVICE_NAME = "ds-data"
    _SERVICE_PROP = "ds_data"
