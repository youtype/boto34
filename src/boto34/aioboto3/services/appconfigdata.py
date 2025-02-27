"""
Wrapper for aioboto3 AppConfigData service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appconfigdata/)

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
    # Returns type annotated aioboto3 AppConfigData client
    appconfigdata_client = session.appconfigdata.client()
    appconfigdata_client: types_aiobotocore_appconfigdata.client.AppConfigDataClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_appconfigdata.client import AppConfigDataClient

from boto34.aioboto3.service_factory import ServiceFactory


class AppConfigDataService(ServiceFactory[AppConfigDataClient]):
    SERVICE_NAME = "appconfigdata"
    _SERVICE_PROP = "appconfigdata"
