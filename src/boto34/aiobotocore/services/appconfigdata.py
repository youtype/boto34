"""
Wrapper for aiobotocore AppConfigData service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfigdata/)

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
    # Returns type annotated aiobotocore AppConfigData client
    async with session.appconfigdata.create_client() as appconfigdata_client:
        appconfigdata_client: types_aiobotocore_appconfigdata.client.AppConfigDataClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_appconfigdata.client import AppConfigDataClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AppConfigDataService(ServiceFactory[AppConfigDataClient]):
    SERVICE_NAME = "appconfigdata"
    _SERVICE_PROP = "appconfigdata"
