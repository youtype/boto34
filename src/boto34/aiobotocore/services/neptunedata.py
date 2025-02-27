"""
Wrapper for aiobotocore NeptuneData service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptunedata/)

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
    # Returns type annotated aiobotocore NeptuneData client
    async with session.neptunedata.create_client() as neptunedata_client:
        neptunedata_client: types_aiobotocore_neptunedata.client.NeptuneDataClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_neptunedata.client import NeptuneDataClient

from boto34.aiobotocore.service_factory import ServiceFactory


class NeptuneDataService(ServiceFactory[NeptuneDataClient]):
    SERVICE_NAME = "neptunedata"
    _SERVICE_PROP = "neptunedata"
